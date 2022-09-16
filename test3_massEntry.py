from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
try:
        # две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
	    #переход по ссылкам
    browser.get("http://suninjuly.github.io/huge_form.html")
        #массовый ввод в одиноковые поля
    elements = browser.find_elements("tag name","input")
    for element in elements: element.send_keys("Рахат лукум")
        #ищем и нажимаем кнопку
    button = browser.find_element("css selector","button.btn")
    button.click()
        #переключаемся на алерт и берем текст сообщения
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally:
        #задержка на посмотреть глазками и закрываем
    time.sleep(5)
    browser.quit()