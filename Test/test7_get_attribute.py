from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
import math                      # берем матемитику для вычислений
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        #переход по ссылкам	
    browser.get("http://suninjuly.github.io/get_attribute.html")
        #берем значесние атрибута	
    treasure = browser.find_element("id","treasure")
    treasure_num = treasure.get_attribute("valuex")
            #проводим вычисления	
    def calc(x):  return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(treasure_num)
        #ищем и вводим в поля значения
    input1 = browser.find_element("id","answer")
    input1.send_keys(y)
        #устанавливаем чек-боксы и радиобаттоны
    option1 = browser.find_element("id","robotCheckbox")
    option1.click()
    option1 = browser.find_element("id","robotsRule")
    option1.click()
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
