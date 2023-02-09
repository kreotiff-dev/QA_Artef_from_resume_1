from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.0_0'
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
driver.find_element_by_link_text("Dynamic Data").click()

modal_window = driver.find_element_by_class_name("cont_box_center")
modal_window_text = modal_window.text
assert "Loading the data Dynamically" in modal_window_text

driver.find_element_by_id("save").click()

time.sleep(5)

img = driver.find_element_by_css_selector("div>img")
img_check = img.get_attribute("src") # создали переменную, в которую поместим значение атрибута
print(img_check) # выводим в консоль значение атрибута

driver.quit()
