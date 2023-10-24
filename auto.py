from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
navegador.get('https://www.hashtagtreinamentos.com/curso-python')
#navegador.maximize_window()


def teste(x):
     #espera satisfazer as condições
     return WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('css selector', x)))


def busca(y):
     return navegador.find_element('css selector', y)


lista = navegador.find_elements(By.ID, 'firstname')
email =
# sleep(2)
# print(len(lista))

busca((lista[1]).send_keys('Val Nicolini'))
busca(lista[1]).send_keys(Keys.ENTER)
busca(lista[1]).send_keys('val_nicolini13@hotmail.com')







# sleep(2)
# navegador.quit()
#pip install ipython





