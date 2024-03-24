from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from time import sleep
from datetime import datetime

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")

navegador.get("https://sistema.hcosta.com.br/hcosta/")
navegador.find_element('xpath', '//*[@id="nome"]').send_keys("silva.valdenir")
navegador.find_element('xpath', '//*[@id="senha"]').send_keys("Nico#1307")
navegador.find_element('xpath', '//*[@id="botao_aceitar"]').click()
navegador.switch_to.window(navegador.window_handles[-1])
sleep(3)
navegador.find_element('xpath', '/html/body/div[6]/ul[5]/li/span').click()
sleep(1)
navegador.find_element('xpath', '/html/body/div[6]/ul[5]/li/ul/li[1]/span').click()
sleep(1)
navegador.find_element('xpath', '//*[@id="m_5_8_8_0"]').click()
sleep(3)
navegador.switch_to.frame('conteudo')
navegador.find_element('xpath', '//*[@id="data_inicial"]').send_keys(data_formatada)
navegador.find_element('xpath', '//*[@id="data_final"]').send_keys(data_formatada)
navegador.find_element('xpath', '/html/body/form/fieldset/ul/li[11]/button').click()
alerta = navegador.switch_to.alert
alerta.accept()
