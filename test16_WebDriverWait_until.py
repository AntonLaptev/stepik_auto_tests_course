from selenium import webdriver   # берем драйвер
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait	 	
from selenium.webdriver.support import expected_conditions as EC
import time                      # берем время для  time.sleep
import math                      # берем матемитику для вычислений
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        #переход по ссылкам	
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
		#ищем кнопку и ждем пока элемент станет равен 100 и жмем
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    button.click()
        #прокручиваем в зону видимости
    button1 = browser.find_element("id","solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
        #вычисляем
    def calc(x):  return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element("id","input_value")
    x = x_element.text
    y = calc(x)
        #вводим вычисленное и жмем кнопку
    input1 = browser.find_element("id","answer")
    input1.send_keys(y)
    button1.click()
        #переключаемся на алерт и берем текст сообщения
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(5)
    browser.quit()