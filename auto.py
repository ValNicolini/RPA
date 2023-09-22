
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=chrome_options)
navegador.maximize_window()


def teste(x):
    return WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath', x)))


def busca(y):
    return navegador.find_element('xpath', y)

navegador.get('https://outlook.office.com/mail/')

teste('//*[@id="i0116"]')

busca('//*[@id="i0116"]').send_keys('silva.valdenir@hcosta.com.br')

teste('//*[@id="idSIButton9"]')
sleep(2)
busca('//*[@id="idSIButton9"]').click()
teste('//*[@id="i0118"]')
busca('//*[@id="i0118"]').send_keys('Nico@123')
teste('//*[@id="idSIButton9"]')
sleep(2)
busca('//*[@id="idSIButton9"]').click()
teste('//*[@id="idSIButton9"]')
busca('//*[@id="idSIButton9"]').click()
teste('//*[@id="id__183"]')
busca('//*[@id="id__183"]').click()
busca('//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[1]').send_keys('santos.william@hcosta.com.br')
busca('//*[@id="TextField675"]').send_keys('Teste')


# sleep(2)
# navegador.quit()

