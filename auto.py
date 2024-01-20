# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.chrome.service import Service
# from time import sleep
#
# from selenium.webdriver.support.ui import WebDriverWait #espera até o elemento aparecer
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import date
# # chrome_options = Options()
# # chrome_options.add_experimental_option("detach", True)
# # service = Service(ChromeDriverManager().install())
# # navegador = webdriver.Chrome(service=service, options=chrome_options)
#
# # opcoes = webdriver.FirefoxOptions()
# # opcoes.add_argument("--headless=new")
#
# navegador = webdriver.Firefox()
# navegador.get('https://sistema.hcosta.com.br/hcosta/index.php')
# #navegador.maximize_window()
#
# data_atual = date.today()
# data_formatada = data_atual.strftime('%d/%m/%Y')
#
#
# def teste(x):
#      #espera satisfazer as condições
#      return WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('css selector', x)))
#
#
# def busca(y):
#      return navegador.find_element('css selector', y)
#
#
# busca('#nome').send_keys('silva.valdenir')
#
# busca('#senha').send_keys('Nico@123')
# busca('#botao_aceitar').click()
# sleep(5)
# lista = navegador.find_elements(By.ID, 'opcoes')
# sleep(3)
# print(len(lista))


# busca('#opcoes > ul:nth-child(5) > li:nth-child(1) > span:nth-child(1)').click()
# busca('#opcoes > ul:nth-child(5) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(1)').click()
# busca('#m_5_8_8_0').click()
# busca('//*[@id="data_inicial"]').send_keys(data_formatada)
# busca('//*[@id="data_final"]').send_keys(data_formatada)
# busca('/html/body/form/fieldset/ul/li[11]/button').click()


#busca((lista[1]).send_keys('Val'))

#teste('//*[@id="senha"]')
#busca('//*[@id="senha"]').send_keys('Nico@123')
#busca('//*[@id="botao_aceitar"]').click()

# sleep(2)
# navegador.quit()
#pip install ipython

# from datetime import date
# data = date.today()
# br = data.strftime('%d/%m/%Y')
# print(br)

