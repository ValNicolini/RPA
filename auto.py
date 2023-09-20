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
navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Nicolini')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('val_nicolini13@hotmail.com')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys('14-998879246')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()
navegador.find_element('xpath',
                       '//*[@id="popup-container"]/div/div/a[1]').click()
sleep(7)
navegador.quit()