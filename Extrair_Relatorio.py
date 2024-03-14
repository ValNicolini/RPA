from playwright.sync_api import sync_playwright, expect
from time import sleep
from datetime import date
data = date.today()
# br = data.strftime('%d/%m/%Y')
with sync_playwright() as p:
        browser = p.firefox.launch(args=["--start-maximised"],headless=False)
        page = browser.new_page(no_viewport=True)

        # Navegar até a página com o formulário
        page.goto('https://sistema.hcosta.com.br/hcosta/')

        page.fill("input[name= 'nome']", 'silva.valdenir')
        page.fill("input[name= 'senha']", 'Nico#1307')
        page.click("button[type= 'submit']")
        sleep(3)
        teste = page.locator('.opcoes')







        browser.close()
