
from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navegar até a página com o formulário
    page.goto('https://todomvc.com/')
