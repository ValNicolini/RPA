# from mouseinfo import mouseInfo
        # mouseInfo()
import self
from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
        browser = p.firefox.launch(args=["--start-maximised"], headless=False)
        page = browser.new_page(no_viewport=True)



        # Navegar até a página com o formulário
        page.goto('https://files-admin.hcosta.com.br/login')

        # Preencher o formulário
        page.fill("input[name='accessKey']", 'A279BJ9KMB6BZ2U5')
        page.fill("input[name='secretKey']", 'K!))9ZCU,!Y}L@,.2)!]UW6}3BZ.}TX-')
        # Submeter o formulário
        page.click("button[type= 'submit']")
        page.click("a[href='/buckets/arquivos-importacao/browse']")

        page.wait_for_timeout(6000)

        x = 1
        for i in range(x):
           sleep(2)
           # Encontrar todos os checkboxes a partir do segundo
           checkboxes = page.query_selector_all('input[type="checkbox"]')[1:11]


        # Iterar sobre os checkboxes e marcá-los
           for checkbox in checkboxes:
                checkbox.click()

           # page.keyboard.press('ArrowDown')
           page.wait_for_timeout(100)
           page.locator('xpath= //*[@id="object-list-wrapper"]/div/div[2]/ul/li[5]/span/button/span[2]').click()
           page.wait_for_timeout(1000)
           page.click("button[label='Delete']")
           page.wait_for_timeout(7000)



        browser.close()
        print(f'Foram excluídos: {x*len(checkboxes)} arquivos!')



