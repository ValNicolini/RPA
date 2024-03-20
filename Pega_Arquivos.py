import shutil
from winotify import Notification, audio
import os
from datetime import datetime

data_atual = datetime.now().strftime('%y%m%d')

def listar_arquivos_por_tipo(diretorio, tipo_arquivo):
    arquivos_do_tipo = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(tipo_arquivo):
            arquivos_do_tipo.append(arquivo)
    return arquivos_do_tipo

def main():
    # Diretório da pasta onde os arquivos estão localizados
    diretorio = r'\\172.25.5.25\rvs\inbox'
    tipo_arquivo = f'{data_atual}0741160000'

    # Listar arquivos do tipo especificado na pasta
    arquivos_tipo_especificado = listar_arquivos_por_tipo(diretorio, tipo_arquivo)

    if arquivos_tipo_especificado:
        alerta = Notification(app_id='Volks', title='ATENÇÃO!', msg='Arquivo Volks chegou!', duration='long',
                             icon=r'C:\xampp\htdocs\GitHub\RPA\images.jpg')
        alerta.set_audio(audio.LoopingAlarm, loop=False)
        alerta.add_actions(label="Volks", launch=r"\\172.25.5.25\rvs\inbox")
        alerta.show()
        print(tipo_arquivo)
    else:
        # Se não houver mais arquivos a serem processados, encerrar a execução
        return

if __name__ == "__main__":
    main()
