from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

driver.maximize_window()
driver.implicitly_wait(5)# говорим WebDriver искать каждый элемент в течение 5 секунд
wait = WebDriverWait (driver, 10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_link_text("My Account").click()

username = driver.find_element_by_id("username")
username.send_keys("tusya1096@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Zxcvbnm0909090")

driver.find_element_by_css_selector("div:nth-child(2)>form>p:nth-child(4)>input:nth-child(3)").click()
driver.quit()

###############################################################################################################


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

driver.maximize_window()
driver.implicitly_wait(5)# говорим WebDriver искать каждый элемент в течение 5 секунд
wait = WebDriverWait (driver, 10)
driver.get("https://practice.automationtesting.in//")

driver.find_element_by_link_text("My Account").click()

username = driver.find_element_by_id("username")
username.send_keys("tusya1096@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Zxcvbnm0909090")

login_btn = driver.find_element_by_name("login")
login_btn.click()

logout = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "nav:nth-child(1)>ul:nth-child(1)>li:nth-child(6)>a"))) # ПРОВЕРИМ ЧТО ЭЛЕМЕНТ LOGOUT ПРИСУТСВУЕТ
driver.quit()

