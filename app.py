import os

restaurantes = [{'Nome':'Pizza','Categoria':'Pizzaria', 'Ativo':False},
                {'Nome':'Tomate', 'Categoria':'Legumes', 'Ativo':True},
                {'Nome':'Arroz', 'Categoria':'Grãos', 'Ativo':False}]


def exibir_nome_do_programa():
    print('SABOR EXPRESS')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
   teste = input('\nDigite uma tecla pra voltar ao menu inicial ou 4 para encerrar: ')
   if int(teste) == 4:
       finalizar_app()
   else:
       main()


def exibir_subtitulo(texto):
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
def finalizar_app():
    #os.system('cls')
    # os.system('clear') 
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro de novos restaurantes:')
   nome_restaurante = input('Nome do restaurante: ')
   nome_categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
   dados_restaurante = {'Nome': nome_restaurante, 'Categoria': nome_categoria, 'Ativo':False}
   restaurantes.append(dados_restaurante)
   print(f'O restaurante {nome_restaurante} foi add com sucesso!')
   voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes:')
    print(f'{'Nome'.ljust(10)} | {'Categoria'.ljust(10)} | {'Status'.ljust(10)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        nome_categoria = restaurante['Categoria']
        estado = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(10)} | {nome_categoria.ljust(10)} | {estado.ljust(10)}')
    voltar_menu_principal()

def alternar_estado_restaurante():
     exibir_subtitulo('Alterando estado do restaurante.')
     nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
     restaurante_encontrado = False
     for restaurante in restaurantes:
         if nome_restaurante == restaurante['Nome']:
             restaurante_encontrado = True
             restaurante['Ativo'] = not restaurante['Ativo']
             mensagem = (f'O restaurante {nome_restaurante} foi ativado com '
                         f'sucesso!' if restaurante['Ativo'] else f'O restaurante {nome_restaurante}'
                         f'foi desativado com sucesso!')
             print(mensagem)
     if not restaurante_encontrado:
         print(f'O restaurante {nome_restaurante} não foi encontrado!')


     voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
           alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()