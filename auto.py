
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

# navegador.get('https://www.google.com.br/?hl=pt-BR')
# navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('cuso em video')
# sleep(2)
# navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
# sleep(2)
# navegador.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[1]/td/div/h3/a').click()
# navegador.find_element('xpath', '//*[@id="cn-accept-cookie"]').click()
# navegador.find_element('xpath','//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input').send_keys('val_nicolini13@hotmail.com')
# navegador.find_element('xpath','//*[@id="uabb-password-field"]').send_keys('11q222q1')
# navegador.find_element('xpath', '//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button').click()
# sleep(2)
# navegador.find_element('xpath', '//*[@id="menu-item-1508"]/a/span').click()
navegador.get('https://outlook.office.com/mail/')
WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="i0116"]')))
navegador.find_element('xpath',  '//*[@id="i0116"]').send_keys('silva.valdenir@hcosta.com.br')
WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="idSIButton9"]')))
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
sleep(2)
navegador.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[1]/td/div/h3/a').click()
navegador.find_element('xpath', '//*[@id="cn-accept-cookie"]').click()
navegador.find_element('xpath','//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input').send_keys('val_nicolini13@hotmail.com')
navegador.find_element('xpath','//*[@id="uabb-password-field"]').send_keys('11q222q1')
navegador.find_element('xpath', '//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button').click()
sleep(2)
navegador.find_element('xpath', '//*[@id="menu-item-1508"]/a/span').click()

sleep(7)
navegador.quit()

