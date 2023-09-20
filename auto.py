from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=chrome_options)
navegador.maximize_window()
navegador.get('https://outlook.office.com/mail/')
navegador.find_element('xpath', '//*[@id="i0116"]').send_keys('silva.valdenir@hcosta.com.br')
navegador.find_element('xpath',
                       '//*[@id="idSIButton9"]').click()
navegador.find_element('xpath', '//*[@id="i0118"]').send_keys('Nico@123')

navegador.find_element('xpath',
                       '//*[@id="id__188"]').click()
navegador.find_element('xpath',
                       '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[1]').send_keys('val_nicolini13@hotmail.com')
navegador.find_element('xpath',
                       '//*[@id="TextField762"]').send_keys('Testando o Robô')
navegador.find_element('xpath',
                       '//*[@id="sonoraIntroHintParent"]/span[1]').send_keys('Email de teste!'
                                                                             'Não responda.'
                                                                             ''
                                                                             'Atenciosamente...')
navegador.find_element('xpath',
                       '//*[@id="id__747"]').click()

navegador.quit()