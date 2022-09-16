from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
import math                      # берем матемитику для вычислений
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
		#переход по ссылкам	
    browser.get("http://suninjuly.github.io/alert_accept.html")
        #ищем и нажимаем кнопку	
    button = browser.find_element("tag name","button")
    button.click()
	    #переключаемся на алерт
    alert = browser.switch_to.alert
    alert.accept()
        #делаем расчет на странице и вводим его
    def calc(x):  return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element("id","input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element("id","answer")
    input1.send_keys(y)
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