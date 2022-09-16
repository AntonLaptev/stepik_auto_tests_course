from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        #скрипты на модалку и изменение имени вкладки	
    browser.execute_script("document.title='Script executing';")
    time.sleep(1)
    browser.execute_script("alert('Robots at work');")    
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    browser.execute_script("document.title='Script executing1';alert('Robots at work1');")
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(3)
    browser.quit()