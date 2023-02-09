from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

first_tab = driver.execute_script("window.open();") # открытие новой вкладки
window_after = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.maximize_window()
driver.implicitly_wait(5)# говорим WebDriver искать каждый элемент в течение 5 секунд
wait = WebDriverWait (driver, 10)
driver.get("http://demo.automationtesting.in/WebTable.html") # на новой вкладке откроем какую-нибудь другую страницу на сайте

driver.find_element_by_link_text("SwitchTo").click()
driver.find_element_by_link_text("Windows").click()
driver.find_element_by_link_text("click").click()

window_after1 = driver.window_handles[2] # создание переменной, где укажем путь к второй вкладке (window_handles[2]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after1) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("https://www.selenium.dev/")
driver.close()

link_check = wait.until(EC.url_to_be("http://demo.automationtesting.in/Index.html"))

driver.switch_to.window(driver.window_handles[2])

namber_of_tabe = wait.until(EC.namber_of_window_to_be[3])

driver.quit()




