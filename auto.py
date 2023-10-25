from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
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

          #LISTAS

nome = navegador.find_elements(By.CSS_SELECTOR, '[name ="firstname"]')
email = navegador.find_elements(By.CSS_SELECTOR, '[name = "email"]')
fone = navegador.find_elements(By.CSS_SELECTOR, '[name = "phone"]')
enviar = navegador.find_elements(By.CSS_SELECTOR, '[class ^= "botao"]')


sleep(2)
print(len(nome))
nome[1].send_keys('Teste')
email[1].send_keys('teste.@hotmail.com')
fone[1].send_keys('14 997303177')
enviar[1].click()
navegador.find_element(By.CSS_SELECTOR, '[name = "s"]').send_keys('Testando')









# sleep(2)
#navegador.quit()
#pip install ipython





