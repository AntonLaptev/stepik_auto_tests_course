from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
import math                      # берем матемитику для вычислений
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        #переход по ссылкам	
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
        #вычисляем значение по формуле и вводим его
    def calc(x):  return str(math.log(abs(12*math.sin(int(x)))))  
    x_element = browser.find_element("id","input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element("id","answer")
    input1.send_keys(y)
        #устанавливаем чек-бокс
    option1 = browser.find_element("id","robotCheckbox")
    option1.click()
        #сдвигаем экран в зону видимости если хотим скролл на конкретное значение - browser.execute_script("window.scrollBy(0, 100);") 
    button = browser.find_element("tag name","button")     
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        #устанавливаем радиобаттон
    option1 = browser.find_element("id","robotsRule")
    option1.click()
	        #кликаем кнопку
    button.click()
            #переключаемся на алерт и берем текст сообщения
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)   
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(5)
    browser.quit()

