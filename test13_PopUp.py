from selenium import webdriver   # берем драйвер
import time                      # берем время для  time.sleep
try:
		# открываем мозиллу
	options = webdriver.FirefoxOptions()
	browser = webdriver.Firefox(options=options)
		# работаем с всплывашкой ОК	
	browser.execute_script("alert('You are not a human');")
		# переключаемся на окно	
	alert = browser.switch_to.alert
		# берем текст
	alert_text = alert.text
	print(alert_text)
		# полюбовались
	time.sleep(2)
		# подтвердили
	alert.accept()
		# работаем с всплывашкой ОК	не ОК
	browser.execute_script("confirm('You are not a robot');")
	confirm = browser.switch_to.alert
	time.sleep(2)
		# жмем отмена
	confirm.dismiss()
		# работаем с всплывашкой ОК	не ОК с полем для ввода
	browser.execute_script("prompt('Ответ на все вопросы',41);")
	time.sleep(2)
	prompt = browser.switch_to.alert
		# вводим текст в поле
	prompt.send_keys("42")
	time.sleep(2)
	prompt.accept()
finally: 
        #задержка на посмотреть глазками и закрываем
    time.sleep(2)
    browser.quit()
