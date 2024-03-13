# from mouseinfo import mouseInfo
        # mouseInfo()
from datetime import datetime
from playwright.sync_api import sync_playwright
from time import sleep

data = datetime.now()
br = data.strftime('%d/%m/%Y')
hora = data.strftime('%H:%M')

with sync_playwright() as p:
        browser = p.chromium.launch() #args=["--start-maximised"],
        page = browser.new_page() #no_viewport=True



        # Navegar até a página com o formulário
        page.goto('https://files-admin.hcosta.com.br/login')

        # Preencher o formulário
        page.fill("input[name='accessKey']", 'A279BJ9KMB6BZ2U5')
        page.fill("input[name='secretKey']", 'K!))9ZCU,!Y}L@,.2)!]UW6}3BZ.}TX-')
        # Submeter o formulário
        page.click("button[type= 'submit']")
        page.click("a[href='/buckets/arquivos-importacao/browse']")

        page.wait_for_timeout(6000)

        # x = 20
        # for i in range(x):
        #    sleep(30)
        #    # Encontrar todos os checkboxes a partir do segundo
        #    checkboxes = page.query_selector_all('input[type="checkbox"]')[1:11]

        # inicio = ("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[1]/div[1]/span/input")
        # Iterar sobre os checkboxes e marcá-los
        x = 1
        for t in range(x):
          y = 10
          for i in range(y):
                i+=1
                page.click(f"xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[{i}]/div[1]/span/input")

                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[2]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[3]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[4]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[5]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[6]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[7]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[8]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[9]/div[1]/span/input")
                # page.click("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[10]/div[1]/span/input")


            # page.keyboard.press('ArrowDown')
            # sleep(0.5)

           # page.keyboard.press('ArrowDown')
          page.wait_for_timeout(2000)
          page.locator('xpath= //*[@id="object-list-wrapper"]/div/div[2]/ul/li[5]/span/button/span[2]').click()
          page.wait_for_timeout(2000)
          page.click("button[label='Delete']")
          page.wait_for_timeout(7000)



        browser.close()
        print(f'Hoje {br}\nÁs {hora}\nForam excluídos: {x*y} arquivos!')



