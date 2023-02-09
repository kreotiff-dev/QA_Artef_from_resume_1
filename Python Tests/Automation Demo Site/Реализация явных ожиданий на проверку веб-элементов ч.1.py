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
driver.find_element_by_link_text("JQuery ProgressBar").click()

button = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.LINK_TEXT, "Close")))

driver.find_element_by_id("downloadButton").click()

some_element= WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonpane>.ui-dialog-buttonset>button"), "Cancel Download"))

driver.find_element_by_css_selector(".ui-dialog-buttonset>button").click()
driver.find_element_by_id("downloadButton").click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-content>.progress-label"), "Complete"))

driver.quit()