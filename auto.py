from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait #espera até o elemento aparecer
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# service = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=service, options=chrome_options)

navegador = webdriver.Firefox()



def teste(x):
     #espera satisfazer as condições
     return WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath', x)))


def busca(y):
     return navegador.find_element('xpath', y)



navegador.get('https://www.hashtagtreinamentos.com/curso-python')
#navegador.maximize_window()
lista = navegador.find_elements(By.XPATH, '//*[@id="firstname"]')

busca((lista[1]).send_keys('Val'))

#teste('//*[@id="senha"]')
#busca('//*[@id="senha"]').send_keys('Nico@123')
#busca('//*[@id="botao_aceitar"]').click()

# sleep(2)
# navegador.quit()






