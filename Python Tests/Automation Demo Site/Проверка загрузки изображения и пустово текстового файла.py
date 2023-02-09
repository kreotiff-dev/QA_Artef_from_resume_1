from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

second_tab = driver.execute_script("window.open();") # открытие новой вкладки
window_after = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.maximize_window()
driver.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
driver.get("http://demo.automationtesting.in/WebTable.html") # на новой вкладке откроем какую-нибудь другую страницу на сайте

driver.find_element_by_link_text("More").click()
driver.find_element_by_link_text("File Upload").click()

file = ('D:\Наташа\Рабочий стол\TBQE6537.jpeg') # переменная = ('C:\название вашей папки\название файла')
upload = driver.find_element_by_id("input-4") # находим селектор кнопки загрузить файл
upload.send_keys(file) # передаём путь к файлу и загружаем

driver.find_element_by_class_name("btn-default.fileinput-remove").click()

file1 = ('D:\Наташа\Рабочий стол\pusto.txt') # переменная = ('C:\название вашей папки\название файла')
upload = driver.find_element_by_id("input-4") # находим селектор кнопки загрузить файл
upload.send_keys(file1) # передаём путь к файлу и загружаем

driver.find_element_by_class_name("close.kv-error-close").click()

driver.quit()