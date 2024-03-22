# from mouseinfo import mouseInfo
        # mouseInfo()
from datetime import datetime
from playwright.sync_api import sync_playwright
from time import sleep

data = datetime.now()
br = data.strftime('%d/%m/%Y')
hora = data.strftime('%H:%M')

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"]) #args=["--start-maximised"],
        page = browser.new_page(no_viewport=True) #no_viewport=True



        # Navegar até a página com o formulário
        page.goto('https://files-admin.hcosta.com.br/login')

        # Preencher o formulário
        page.locator("#accessKey").fill('A279BJ9KMB6BZ2U5')
        page.locator("#secretKey").fill('K!))9ZCU,!Y}L@,.2)!]UW6}3BZ.}TX-')
        # Submeter o formulário
        page.click("#do-login")
        page.click("a[href='/buckets/arquivos-importacao/browse']")

        page.wait_for_timeout(6000)

        # x = 2
        # for t in range(x):
        #   y = 10
        x = 50
        for i in range(x):
            i+=1
            sleep(0.1)
            seletor = f'''div.ReactVirtualized__Grid__innerScrollContainer div[aria-rowindex="{i}"] input'''
            page.click(seletor)
            sleep(0.1)
              # f"xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[{i}]/div[1]/span/input"

        page.wait_for_timeout(2000)
        page.locator('xpath= //*[@id="object-list-wrapper"]/div/div[2]/ul/li[5]/span/button/span[2]').click()
        page.wait_for_timeout(2000)
        page.click("button[label='Delete']")
        page.wait_for_timeout(7000)

        browser.close()
        print(f'Hoje {br}\nÁs {hora}\nForam excluídos: {x} arquivos!')



