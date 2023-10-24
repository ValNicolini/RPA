from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait #espera até o elemento aparecer
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# service = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=service, options=chrome_options)

# opcoes = webdriver.FirefoxOptions()
# opcoes.add_argument("--headless=new")

navegador = webdriver.Firefox()
navegador.get('https://www.hashtagtreinamentos.com/cursos-hashtag-programacao?')
#navegador.maximize_window()


def teste(x):
     #espera satisfazer as condições
     return WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath', x)))


def busca(y):
     return navegador.find_element('css selector', y)


busca('.wp-image-13719 > img:nth-child(2)').click()
# sleep(1)
# busca('div.bloco-textoinput-formulario-excel-empe:nth-child(8) > input:nth-child(2)').send_keys('Val Nicolini')


lista = navegador.find_elements(By.ID, 'firstname')
sleep(5)
print(len(lista))







# sleep(2)
# navegador.quit()
#pip install ipython





