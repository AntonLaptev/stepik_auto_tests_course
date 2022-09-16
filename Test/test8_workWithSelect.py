from selenium import webdriver      # берем драйвер
from selenium.webdriver.support.ui import Select   
import time                         # берем время для  time.sleep
import math                         # берем матемитику для вычислений
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
            #переход по ссылкам	
    browser.get("http://suninjuly.github.io/selects1.html")
            #берем числа и считаем сумму	
    num1 = browser.find_element("id","num1")
    x = num1.text
    num2 = browser.find_element("id","num2")
    y = num2.text
    z = int(x) + int(y) 
    print(z)
            #выбираем получившееся число в выпадающем списке	
    select = Select(browser.find_element("tag name","select"))
    select.select_by_value(str(z))
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