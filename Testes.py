
# from mouseinfo import mouseInfo
#
# mouseInfo()

from playwright.sync_api import sync_playwright



with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) #args=["--start-maximised"]
        page = browser.new_page() #no_viewport=True



        # Navegar até a página com o formulário
        page.goto('https://donnagusta.onpedido.com.br/')

        page.wait_for_timeout(2000)
