from selenium.




url = 'https://selenium.dunossauro.live/aula_04_b.html'
browser = webdriver.Firefox()
browser.get(url)


def find_by_text(browser, tag, text):
    elementos = browser.find_elements(By.TAG_NAME, tag)
    for elemento in elementos:
         if elemento.text == text:
              return elemento


caixas = ['um', 'dois', 'tres', 'quatro']
for texto in caixas :
     find_by_text(browser, 'div', texto).click()

for texto in caixas:
     sleep(0.5)
     browser.back()

for texto in caixas:
     sleep(0.5)
     browser.forward()
