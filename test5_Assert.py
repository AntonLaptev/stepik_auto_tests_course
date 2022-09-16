from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
try:
        # две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        # переход по ссылкам    
    browser.get("http://suninjuly.github.io/registration1.html")
        #массовый ввод в одиноковые поля
    elements = browser.find_elements("class name","form-control")
    for element in elements: element.send_keys("М1")
        #ищем и нажимаем кнопку
    button = browser.find_element("css selector","button.btn")
    button.click()
        #ждем появления текста и делаем ассерт
    time.sleep(1)
    welcome_text_elt = browser.find_element("tag name","h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(5)
    browser.quit()