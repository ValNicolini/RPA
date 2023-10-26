from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait #espera até o elemento aparecer
from selenium.webdriver.support import expected_conditions as EC
from datetime import date



# chrome_options.add_experimental_option("detach", True)
# service = Service(GeckoDriverManager().install())



url = 'https://sistema.hcosta.com.br/hcosta/index.php'
opcoes = Options()
opcoes.add_argument('--headless')
opcoes = False
navegador = webdriver.Firefox(options=opcoes)
navegador.get(url)


# waitAbrirSistema.until(EC.number_of_windows_to_be(2))
# driver.switch_to.window(driver.window_handles[1])

navegador.find_element(By.CSS_SELECTOR, '[name="nome"]').send_keys('silva.valdenir')
navegador.find_element(By.CSS_SELECTOR, '[name="senha"]').send_keys('Nico@123')
navegador.find_element(By.CSS_SELECTOR, '[id="botao_aceitar"]').click()
navegador.get('https://sistema.hcosta.com.br/hcosta/sistema.php')
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#opcoes > ul:nth-child(5) > li:nth-child(1) > span:nth-child(1)')))
navegador.switch_to.window(navegador.window_handles[1])
navegador.find_element(By.CSS_SELECTOR, '#opcoes > ul:nth-child(5) > li:nth-child(1) > span:nth-child(1)').click()
# navegador.find_element(By.CSS_SELECTOR, '#opcoes > ul:nth-child(5) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(1)').click()
# navegador.find_element(By.CSS_SELECTOR, '#opcoes > ul:nth-child(5) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(1)').click()
# navegador.find_element(By.CSS_SELECTOR, '#data_inicial').send_keys('26/10/2023')
# navegador.find_element(By.CSS_SELECTOR, '#data_final').send_keys('26/10/2023')
# navegador.find_element(By.CSS_SELECTOR, '.botao_a_direita').click()