from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
import math                      # берем матемитику для вычисления ссылки на странице
try:
        # две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    browser = webdriver.Chrome(options=options)
        #переход по ссылкам
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element("link text",str(math.ceil(math.pow(math.pi, math.e)*10000))) #вычисление ссылки на странице
    link.click()
        #ищем и вводим в поля значения
    input1 = browser.find_element("tag name","input")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name","last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element("class name","city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element("id","country")
    input4.send_keys("Russia")
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