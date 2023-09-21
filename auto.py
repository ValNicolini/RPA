# pip install pyautogui pillow mouseinfo
# from mouseinfo import mouseInfo
# mouseInfo()

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
navegador.get('https://www.cursoemvideo.com/')
navegador.find_element('xpath', '//*[@id="menu-item-42376"]/a/span').click()
navegador.execute_script("window.scrollTo(0, Y)")
# navegador.find_element('xpath','//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input').send_keys('val_nicolini13@hotmail.com')
# navegador.find_element('xpath', '//*[@id="uabb-password-field"]').send_keys('11q222q1')
# navegador.find_element('xpath','//*[@id="cn-accept-cookie"]').click()
# navegador.find_element('xpath','//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button/span').click()

# navegador.find_element('xpath',
#                        '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[1]').send_keys('val_nicolini13@hotmail.com')
# navegador.find_element('xpath',
#                        '//*[@id="TextField762"]').send_keys('Testando o Robô')
# navegador.find_element('xpath',
#                        '//*[@id="sonoraIntroHintParent"]/span[1]').send_keys('Email de teste!'
#                                                                              'Não responda.'
#                                                                              ''
#                                                                              'Atenciosamente...')
# navegador.find_element('xpath',
#                        '//*[@id="id__747"]').click()
#
# navegador.quit()