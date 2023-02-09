import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options) # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.get("http://demo.automationtesting.in/WebTable.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

time.sleep(3) # ставим ожидание 3 секунд, чтобы страница успела прогрузиться

driver.find_element_by_link_text("SwitchTo").click()
driver.find_element_by_link_text("Alerts").click()

time.sleep(3)

driver.find_element_by_class_name("btn.btn-danger").click()

#alert_script = driver.execute_script("alert('I am an alert box!');") # вызываем окно alert
alert = driver.switch_to.alert # переключаемся в область окна alert; обратите внимание, “()” после switch_to.alert не нужны
alert_text = alert.text # получаем текст с помощью команды .text
print(alert_text) # выводим содержимое в консоли
alert.accept() # нажимаем на “OK” в окне alert

second_tab = driver.execute_script("window.open();") # открытие новой вкладки
window_after = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://demo.automationtesting.in/WebTable.html") # на новой вкладке откроем какую-нибудь другую страницу на сайте

driver.find_element_by_link_text("SwitchTo").click()
driver.find_element_by_link_text("Alerts").click()
driver.find_element_by_link_text("Alert with OK & Cancel").click()

time.sleep(3)

driver.find_element_by_class_name("btn.btn-primary").click()
confirm = driver.switch_to.alert
confirm.dismiss() # то же самое, что и при нажатии пользователем кнопки "Отмена".

time.sleep(3)

third_tab = driver.execute_script("window.open();") # открытие новой вкладки
window_after = driver.window_handles[2] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://demo.automationtesting.in/WebTable.html") # на новой вкладке откроем какую-нибудь другую страницу на сайте

time.sleep(3)

driver.find_element_by_link_text("SwitchTo").click()
driver.find_element_by_link_text("Alerts").click()
driver.find_element_by_link_text("Alert with Textbox").click()
driver.find_element_by_class_name("btn.btn-info").click()
time.sleep(3)

prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()
time.sleep(3)
driver.quit()