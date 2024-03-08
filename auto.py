
from playwright.sync_api import sync_playwright

from  require import require

chromium = require('playwright')
expect = require('expect')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # Navegar até a página com o formulário
    page.goto('http://todomvc.com/examples/react/#/')
