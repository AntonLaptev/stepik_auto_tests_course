from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
import os

try:
		# две строки ниже нужны чтобы не ругался на usb в хром драйвере, не мешает, чисто убрать ошибку из лога,ремонтить не будут все равно
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
        #переход по ссылкам	
    browser.get("http://suninjuly.github.io/file_input.html")
        #ищем и вводим в поля значения   
    input1 = browser.find_element("name","firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name","lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element("name","email")
    input3.send_keys("2@2.com")
        #загружаем файл   
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir,'forUploadTest.txt')  
    file = browser.find_element("id","file") 
    file.send_keys(file_path)
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
