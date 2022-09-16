from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
	        #переход по ссылкам	
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
	        #ищем и нажимаем кнопку !!!!будет ошибка из-за перекрытия
    button = browser.find_element("tag name","button")
    button.click() 
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(5)
    browser.quit()
