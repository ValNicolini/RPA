from playwright.sync_api import sync_playwright
from time import sleep
from datetime import date

# with sync_playwright() as p:
#     browser = p.firefox.launch(args=["--start-maximised"], headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     # Navegar até a página com o formulário
#     page.goto('https://sistema.hcosta.com.br/hcosta/')
#
#     page.fill("input[name='nome']", 'silva.valdenir')
#     page.fill("input[name='senha']", 'Nico#1307')
#     page.click("button[type='submit']")
#     sleep(3)
#
#     # Alternar para a última página aberta
#     last_page = context.pages[-1]
#     context.page = last_page
#     sleep(3)
#     page.click('/html/body/div[6]/ul[3]/li/span')
#
#     browser.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep

data_atual = date.today().strftime('%d%m%Y')

# Inicializar o driver do Selenium (neste caso, estou usando o Firefox)
navegador = webdriver.Firefox()

# Navegar até a página com o formulário
navegador.get('https://sistema.hcosta.com.br/hcosta/')

# Preencher o formulário e fazer login
navegador.find_element(By.NAME, 'nome').send_keys('silva.valdenir')
navegador.find_element(By.NAME, 'senha').send_keys('Nico#1307')
navegador.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


# Alternar para a última janela ou aba aberta
navegador.switch_to.window(navegador.window_handles[-1])

# Esperar um pouco para garantir que a troca de janela foi concluída
sleep(1)
navegador.find_element('xpath', '/html/body/div[6]/ul[5]/li/span').click()
sleep(1)
navegador.find_element('xpath', '/html/body/div[6]/ul[5]/li/ul/li[1]/span').click()
sleep(1)
navegador.find_element('xpath','//*[@id="m_5_8_8_0"]').click()
sleep(1)

navegador.find_element('xpath', '//*[@id="data_inicial"]').click()
navegador.find_element('xpath', '//*[@id="data_final"]').send_keys('22032024')
navegador.find_element('xpath','/html/body/form/fieldset/ul/li[11]/button').click()
sleep(1)

# Agora você está na última janela ou aba
print(navegador.title)

# Fechar o navegador
navegador.quit()
print(data_atual)