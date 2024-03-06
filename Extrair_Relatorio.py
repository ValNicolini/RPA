from playwright.sync_api import sync_playwright
from time import sleep
from datetime import date
data = date.today()
# br = data.strftime('%d/%m/%Y')
with sync_playwright() as p:
        browser = p.firefox.launch(headless= False,slow_mo=50)
        page = browser.new_page()

        # Navegar até a página com o formulário
        page.goto('https://sistema.hcosta.com.br/hcosta/')

        page.fill("input[name= 'nome']", 'silva.valdenir')
        page.fill("input[name= 'senha']", 'Nico#1307')
        page.click("button[type= 'submit']")
        page.locator('xpath=/html/body/div[7]/a[1]/img').click()


        # page.locator("xpath= /html/body/div[6]/ul[5]/li/ul/li[2]/span").click()
        # page.locator('xpath= //*[@id="object-list-wrapper"]/div/div[2]/ul/li[5]/span/button/span[2]').click()
        # page.click("button[type= 'submit']")
        # page.click("a[href='/buckets/arquivos-importacao/browse']")
        sleep(3)




        browser.close()
