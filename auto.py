
from playwright.sync_api import sync_playwright
from time import sleep



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://todomvc.com/')
    context = browser.new_context(color_scheme='dark'
                                   # record_video_dir='Video',
                                  # viewport={'width':800, 'height': 1000}
                                  )

    # # Navegar até a página com o formulário
    # page = context.new_page()
    # page.goto('https://todomvc.com/')
    # sleep(3)
    page.screenshot(path='Foto.png')
    #
    # print(page.title())
    # print(p.devices.keys())
    # request = p.request.new_context()
    # response = request.get('https://todomvc.com/')
    # print(response.status)
    # print(response.status_text)
    # print(response.text())

    browser.close()


