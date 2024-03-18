import shutil
from datetime import date
data = date.today()
br = data.strftime('%d%m%Y')
caminho_origem = r'C:\Users\silva.valdenir\Downloads\CNAB_BF\Screenshot.png'
caminho_destino = fr'C:\Users\silva.valdenir\Downloads\ACIONAMENTOS'

shutil.move(caminho_origem, caminho_destino)