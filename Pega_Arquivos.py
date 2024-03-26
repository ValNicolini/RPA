from winotify import Notification, audio
import schedule
from time import sleep
import os
from datetime import datetime

data_atual = datetime.now().strftime('%y%m%d')
# while True:
#     schedule.run_pending()
#     sleep(10)
def listar_arquivos(diretorio):
        arquivos = []
        for arquivo in os.listdir(diretorio):
            arquivos.append(arquivo)
        return arquivos


def caminho():
        # Local dos arquivos
        diretorio = r'\\172.25.5.25\rvs\inbox'

        arquivo = data_atual

            # Listar arquivos
        arquivos = listar_arquivos(diretorio)
        # Loop infinito
        # while True:
        for r in arquivos:
           if arquivo in r:
            alerta = Notification(app_id='Volks', title='ATENÇÃO!', msg='Arquivo Volks chegou!', duration='long',
                                          icon=r'C:\xampp\htdocs\GitHub\RPA\images.jpg')
            alerta.set_audio(audio.LoopingAlarm, loop=False)
            alerta.add_actions(label="Volks", launch=r"\\172.25.5.25\rvs\inbox")
            alerta.show()
            print(f'\n-----------------------------------------'
                  f'\n{r}'
                  f'\n-----------------------------------------')
            # return  # Parar a execução quando o arquivo for encontrado




        # Aguarda e verifica novamente
        #      sleep(10)


if __name__ == "__main__":
      caminho()
