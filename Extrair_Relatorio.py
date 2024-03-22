from playwright.sync_api import sync_playwright
from time import sleep
from datetime import date

with sync_playwright() as p:
    browser = p.firefox.launch(args=["--start-maximised"], headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navegar até a página com o formulário
    page.goto('https://sistema.hcosta.com.br/hcosta/')

    page.fill("input[name='nome']", 'silva.valdenir')
    page.fill("input[name='senha']", 'Nico#1307')
    page.click("button[type='submit']")
    sleep(3)

#     # Alternar para a última página aberta
    last_page = context.pages[-1]
    context.page = last_page
    sleep(3)
    page.click("/html/body/div[6]/ul[5]/li/span")

#
browser.close()
