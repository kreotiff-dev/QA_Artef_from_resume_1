import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver

driver = webdriver.Chrome() # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.get("https://demo.automationtesting.in/Register.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

time.sleep(3) # ставим ожидание 3 секунд, чтобы страница успела прогрузиться

firstname = driver.find_element_by_css_selector(".form-group:nth-child(1)>.col-md-4.col-xs-4.col-sm-4:nth-child(2)>.ng-invalid-required") # объявляем переменную login, задаём ей значение селектора поля логин
firstname.send_keys("dfvsd") # команда send_keys("значение") – нужна для ввода информации в поле

lastname = driver.find_element_by_css_selector(".form-group:nth-child(1)>.col-md-4.col-xs-4.col-sm-4:nth-child(3)>.ng-invalid-required")
lastname.send_keys("DVDVD")

mail = driver.find_element_by_class_name("form-control.ng-pristine.ng-valid-email")
mail.send_keys("tusya1096@mail.ru")

phone = driver.find_element_by_class_name("form-control.ng-pristine.ng-invalid.ng-invalid-required.ng-valid-pattern")
phone.send_keys("1234569632")

driver.find_element_by_css_selector("[value=Male]").click()

year = driver.find_element_by_id("yearbox")
select = Select(year) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("1996")

month = driver.find_element_by_css_selector(".form-group:nth-child(11)>.col-sm-3:nth-child(3)>.ng-invalid-required")
select = Select(month) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("January")

day = driver.find_element_by_id("daybox")
select = Select(day) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("10")

password = driver.find_element_by_id("firstpassword")
password.send_keys("Qasdfg23")

confirmpass = driver.find_element_by_id("secondpassword")
confirmpass.send_keys("Qasdfg23")

file = ('D:\Наташа\Рабочий стол\TBQE6537.jpeg') # переменная = ('C:\название вашей папки\название файла')
upload = driver.find_element_by_id("imagesrc") # находим селектор кнопки загрузить файл
upload.send_keys(file) # передаём путь к файлу и загружаем

button = driver.find_element_by_id("submitbtn")
driver.execute_script("window.scrollBy(0, 300);", button) # автоматически проскроллили до зоны видимости кнопки
button.click()

driver.quit()