import shutil
from winotify import Notification, audio
import os
from datetime import datetime

# Diretório da pasta onde os arquivos estão localizados
# diretorio = r'\\172.25.5.25\rvs\inbox'
data_atual = datetime.now().strftime('%y%m%d')

# Listar todos os arquivos na pasta
# arquivos = os.listdir(diretorio)


# caminho_origem = r'C:\Users\silva.valdenir\Downloads\CNAB_BF\Screenshot.png'
# caminho_destino = fr'C:\Users\silva.valdenir\Downloads\ACIONAMENTOS'
#
# shutil.move(caminho_origem, caminho_destino)

def listar_arquivos_por_tipo(diretorio, tipo_arquivo):
    arquivos_do_tipo = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(tipo_arquivo):
            arquivos_do_tipo.append(arquivo)
    return arquivos_do_tipo

def main():
    # Diretório da pasta onde os arquivos estão localizados
    diretorio = r'\\172.25.5.25\rvs\inbox'
    tipo_arquivo = f'.{data_atual}0907520000'

    # Listar arquivos do tipo especificado na pasta
    while True:
           arquivos_tipo_especificado = listar_arquivos_por_tipo(diretorio, tipo_arquivo)

           if arquivos_tipo_especificado:
               alerta = Notification(app_id='Volks', title='ATENÇÃO!', msg='Arquivo Volks chegou!', duration='long',
                                     icon=r'C:\xampp\htdocs\GitHub\RPA\images.jpg')
               alerta.set_audio(audio.LoopingAlarm, loop=False)
               alerta.add_actions(label="Volks", launch=r"\\172.25.5.25\rvs\inbox")
               alerta.show()
               break
           else:
               return




if __name__ == "__main__":
     main()
