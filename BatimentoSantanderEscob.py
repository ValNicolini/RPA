import pyodbc
import pandas as pd
import os
import random
from datetime import datetime, timedelta
import locale
def arquivo_analito(quanti_dias): 
    Quantos_dias_para_Tras = quanti_dias
    pasta_acionamentos = r'\\fileserver\Arquivo de Acionamentos\Santander Escob'
    sub_pastas = os.listdir(pasta_acionamentos)
    meses = {
        'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6,
        'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12
    }
    for i,o in zip(sub_pastas,range(len(sub_pastas))):
        if i == '-':
            sub_pastas.pop(o)
    datas_convertidas = [
        datetime(year=int(data.split('-')[1]), month=meses[data.split('-')[0]], day=1)
        for data in sub_pastas
    ]
    data_mais_recente = max(datas_convertidas)
    indice_data_mais_recente = datas_convertidas.index(data_mais_recente)
    data_mais_recente_original = sub_pastas[indice_data_mais_recente]
    arquivos = os.listdir(os.path.join(pasta_acionamentos,data_mais_recente_original))
    arquivos.sort()  
    datas_validas = []
    for arquivo in arquivos:
        if datetime(year=int(arquivo.split('-')[2].split('.')[0]), month=int(arquivo.split('-')[1]), day=int(arquivo.split('-')[0])).weekday() != 6:
            datas_validas.append(arquivo)
    arquivos = datas_validas
    data_atual = datetime.now()
    diferenca_de_dias = timedelta(days=Quantos_dias_para_Tras)
    data = (data_atual - diferenca_de_dias).strftime("%d%m%Y")
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    mes_atual_nome = (data_atual - diferenca_de_dias).strftime('%B').capitalize()
    datas = arquivos[-1][:-4].split('-')
    data_desejada = datas[-1] + '-' + datas[-2] + '-' + datas[0]
    dia = data[0:2]
    mes = data[2:4]
    df_acionamentos = pd.read_csv( os.path.join(pasta_acionamentos,data_mais_recente_original,arquivos[-Quantos_dias_para_Tras])   ,dtype=str, sep= ';')
    df_acionamentos = df_acionamentos[~df_acionamentos['evento'].str.contains('MULTICANAL|ENVIO DE SMS|ENVIO DE EMAIL|CAIXA POSTAL')]
    conn_str = 'DRIVER={SQL Server};SERVER=10.10.30.30;DATABASE=Antares;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)
    query = f'''
    SELECT [DATA]
        ,[Atendente]
        ,[HoraInicio]
        ,[HoraFim]
        ,[Resultado]
        ,[Telefone]
        ,[contrato]
        ,[Documento]
        ,[finalizacao]
    FROM [Antares].[dbo].[bilhetes]
    WHERE [Data] = '{data_desejada}'
    AND [ModoDiscagem] = 'Receptivo'
    AND ACD = '4009'
    '''
    dados = pd.read_sql(query, conn)
    conn.close()
    dados['hora_minuto'] = dados['HoraFim'].str[:5]
    df_acionamentos['hora_minuto'] = df_acionamentos['hora'].str[:5]
    lista_operadores = list(dados['Atendente'].drop_duplicates())
    arquivo_excel = pd.DataFrame()
    loop_nomes = 0
    while loop_nomes < len(lista_operadores):
        teste_df_acionamentos = df_acionamentos[df_acionamentos['nome_usuario'] == lista_operadores[loop_nomes]]
        teste_dados = dados[dados['Atendente'] == lista_operadores[loop_nomes]]
        loop_geral = 0
        while loop_geral < len(teste_dados):
            controle_loop = 0
            while controle_loop < len(teste_df_acionamentos):
                if int(teste_dados.iloc[loop_geral,-1][0:2]) == int(teste_df_acionamentos.iloc[controle_loop,-1][0:2]):
                    resultado = int(teste_df_acionamentos.iloc[controle_loop,-1][3:5]) - int(teste_dados.iloc[loop_geral,-1][3:5])
                    if resultado <= 4:
                        nova_linha = {'Hora': [teste_dados.iloc[loop_geral,-1]], 'Operador': [teste_dados.iloc[loop_geral,1]], 'Documento': [teste_df_acionamentos.iloc[controle_loop,5]], 'NOME DO EVENTO':[teste_df_acionamentos.iloc[controle_loop,6]]}
                        nova_linha_df = pd.DataFrame(nova_linha)
                        arquivo_excel = pd.concat([arquivo_excel, nova_linha_df], ignore_index=True) 
                controle_loop += 1
            loop_geral += 1
        loop_nomes += 1
    try:
        arquivo_excel['concat'] = arquivo_excel['Hora'] + arquivo_excel['Operador']
    except:
        print('Não teve ligação cabivel de realizar o tratamento.')
        input('Tratamento concluido, aperte "Enter" para sair.')
        exit() 
    dados['concat'] = dados['hora_minuto'] + dados['Atendente']
    Documento = arquivo_excel['Documento']
    concat = arquivo_excel['concat']
    NOME_DO_EVENTO = arquivo_excel['NOME DO EVENTO']
    dicionario_concat = {}
    for i,j in zip(concat, Documento):
        dicionario_concat[i] = j
    dicionario_NOME_DO_EVENTO = {}
    for i,j in zip(concat, NOME_DO_EVENTO):
        dicionario_NOME_DO_EVENTO[i] = j
    dados['Documento'] = dados['concat'].map(dicionario_concat)   
    dados['NOME DO EVENTO'] = dados['concat'].map(dicionario_NOME_DO_EVENTO) 
    Resultado_com_documentos = dados
    Resultado_com_documentos['num_caracteres'] = Resultado_com_documentos['Documento'].apply(lambda x: len(str(x)) if x is not None else 0)
    Resultado_com_documentos['TIPO_PESSOA'] = Resultado_com_documentos['num_caracteres'].replace({3: '',14: 'PF', 18: 'PJ'})
    Resultado_com_documentos['CPF_CNPJ'] = Resultado_com_documentos['Documento'].str.replace(r'\.', '', regex=True).str.replace(r'-', '', regex=True).str.replace(r'/', '', regex=True)
    Resultado_com_documentos['SEGMENTO'] = 'VAREJO'
    Resultado_com_documentos['SITE'] = 'HCOSTA_ESCOB'
    Resultado_com_documentos['DATA'] = pd.to_datetime(Resultado_com_documentos['DATA'])
    Resultado_com_documentos['DATA'] = Resultado_com_documentos['DATA'].dt.strftime('%d/%m/%Y')
    Resultado_com_documentos["HR_ATENDIMENTO"] = Resultado_com_documentos["HoraInicio"].str[:8]
    Resultado_com_documentos["HR_ENCERRAMENTO"] = Resultado_com_documentos["HoraFim"].str[:8]
    Resultado_com_documentos["TRANSFERENCIA"] = ''
    Resultado_com_documentos["TELEFONE_A"] = Resultado_com_documentos["Telefone"]
    Resultado_com_documentos["TELEFONE_B"] = '08007604040'
    Resultado_com_documentos["URA"] = '0800 EPS'
    Resultado_com_documentos["FILA"] = ''
    Resultado_com_documentos['Tempo total da chamada'] = ''
    Resultado_com_documentos['IDENTIFICADO'] = ''
    Resultado_com_documentos['TEMPO_TABULANDO'] = ''
    for i in range(len(Resultado_com_documentos)):
        resultado_segundo =  int(Resultado_com_documentos.iloc[i,3][6:8]) - int(Resultado_com_documentos.iloc[i,2][6:8])
        resultado_minuto =  int(Resultado_com_documentos.iloc[i,3][3:5]) - int(Resultado_com_documentos.iloc[i,2][3:5])
        resultado_hora = int(Resultado_com_documentos.iloc[i,3][0:2]) - int(Resultado_com_documentos.iloc[i,2][0:2])
        Resultado_final = resultado_segundo + (resultado_minuto * 60) + (resultado_hora * 60 * 60)
        minutos = Resultado_final/60
        horas = Resultado_final/60/60
        Resultado_com_documentos.iloc[i,-1] = f'{int(horas):02}:{int(minutos):02}:{Resultado_final - int(minutos)*60:02}'
        Resultado_com_documentos.iloc[i,-3] = Resultado_final
        if Resultado_final > 30:
            Resultado_com_documentos.iloc[i,-2] = "S"
        else:
            Resultado_com_documentos.iloc[i,-2] = "N"
    Resultado_com_documentos['HR_ENTRADA'] = Resultado_com_documentos['HoraInicio'].str[:8] 
    Resultado_com_documentos['HR_ENTRADA'] = pd.to_datetime(Resultado_com_documentos['HR_ENTRADA'], format='%H:%M:%S')
    def subtract_random_seconds(dt):
        seconds_to_subtract = random.choice([1, 2])
        return dt - timedelta(seconds=seconds_to_subtract)
    Resultado_com_documentos['HR_ENTRADA'] = Resultado_com_documentos['HR_ENTRADA'].apply(subtract_random_seconds)
    Resultado_com_documentos['HR_ENTRADA'] = Resultado_com_documentos['HR_ENTRADA'].dt.time
    Resultado_com_documentos['HR_ENTRADA'] = Resultado_com_documentos['HR_ENTRADA']
    depara_tab = pd.read_csv(r'\\fileserver\Share-Geral\Batimento Santander Escob\de para santander atualizado.csv', dtype=str, encoding='latin1', sep= ';')
    tabulação = list(depara_tab['desc_hcosta'])
    desc_banco = list(depara_tab['desc_banco'])
    codigo_banco = list(depara_tab['codigo_banco'])
    dicionario_desc_banco = {}
    for i,j in zip(tabulação, desc_banco):
        dicionario_desc_banco[i] = j
    dicionario_codigo_banco = {}
    for i,j in zip(tabulação, codigo_banco):
        dicionario_codigo_banco[i] = j
    Resultado_com_documentos['CODIGO_DESCULPA'] = Resultado_com_documentos['NOME DO EVENTO'].map(dicionario_desc_banco)
    Resultado_com_documentos['FINALIZACAO'] = Resultado_com_documentos['NOME DO EVENTO'].map(dicionario_codigo_banco)
    capacity = pd.read_excel(r'\\fileserver\Share-Geral\Arquivo de capacity santander\CAPACITY ESCOB.xlsx')
    LOGIN = list(capacity['LOGIN SISTEMA'].str.lower())
    NOME = list(capacity['OPERADOR'])
    dicionario_LOGIN = {}
    for i,j in zip(LOGIN, NOME):
        dicionario_LOGIN[i] = j
    Resultado_com_documentos['OPERADOR'] = Resultado_com_documentos['Atendente'].map(dicionario_LOGIN)
    Resultado_com_documentos['OFERTA'] = 'PREJUÍZO'
    Resultado_com_documentos = Resultado_com_documentos[['SEGMENTO','SITE','DATA','HR_ENTRADA','TELEFONE_A','TELEFONE_B','URA','CPF_CNPJ','IDENTIFICADO','TIPO_PESSOA','FILA','OFERTA','TRANSFERENCIA','HR_ATENDIMENTO','HR_ENCERRAMENTO','TEMPO_TABULANDO','OPERADOR','FINALIZACAO','CODIGO_DESCULPA']]
    Resultado_com_documentos.loc[:, ('FINALIZACAO')] = Resultado_com_documentos['FINALIZACAO'].replace(['AA','AB','BL','NA','SD',],'')
    Resultado_com_documentos = Resultado_com_documentos.sort_values('FINALIZACAO')
    Resultado_com_documentos = Resultado_com_documentos[Resultado_com_documentos['FINALIZACAO'].astype(str).str.len() > 1]
    Resultado_com_documentos.to_csv(r'\\fileserver\Share-Geral\Batimento Santander Escob' + '\\' + mes_atual_nome + ' resultado'+ '\\' + 'ANALITICO_RECEPTIVO_HCOSTA_ESCOB_' + dia + '.' + mes +  '.txt', sep=';',index=False)
    Resultado_com_documentos.to_excel(r'\\fileserver\Share-Geral\Batimento Santander Escob' + '\\' + mes_atual_nome + ' resultado'+ '\\' + 'ANALITICO_RECEPTIVO_HCOSTA_ESCOB_' + dia + '.' + mes  +'.xlsx', index=False)
    data_frame_geral = pd.DataFrame()
    pasta = r'\\fileserver\Share-Geral\Batimento Santander Escob' + '\\' + mes_atual_nome + ' resultado' 
    subpastas = os.listdir(pasta)
    texto_para_deletar = ".txt"
    nova_lista = []
    for linha in subpastas:
        if texto_para_deletar not in linha:
            nova_lista.append(linha)
    subpastas = nova_lista
    for i in subpastas:
        arquivo = pd.read_excel(pasta + '\\' + i, dtype='str')
        data_frame_geral = pd.concat([data_frame_geral,arquivo], ignore_index=True)
    caminho_da_pasta = r'\\fileserver\Share-Geral\Arquivo receptivo Santander' + '\\' + str((data_atual - diferenca_de_dias).year)  + '\\' + mes_atual_nome  + '\\' + str((data_atual - diferenca_de_dias).day)
    if not os.path.exists(caminho_da_pasta):
        os.makedirs(caminho_da_pasta)
    data_frame_geral.to_csv(caminho_da_pasta + '\\' + 'ANALITICO_RECEPTIVO_HCOSTA_ESCOB_' + mes + '.txt', sep=';',index=False)
if datetime.now().weekday() == 0:
    arquivo_analito(3)
    arquivo_analito(2)
else:
    arquivo_analito(1)
input('Tratamento concluido, aperte "Enter" para sair.')
exit()