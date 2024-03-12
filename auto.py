
# from playwright.sync_api import sync_playwright
#
#
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#
#     # Navegar até a página com o formulário
#     page.goto('https://todomvc.com/')


inicio = '''("xpath= //*[@id='object-list-wrapper']/div/div[1]/div[2]/span/div/div[1]/div/div[2]/div/div[1]/div[1]/span/input")'''

print(inicio[80:100])