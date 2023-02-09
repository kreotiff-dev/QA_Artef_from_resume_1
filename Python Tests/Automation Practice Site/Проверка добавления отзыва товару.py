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

driver.execute_script("window.scrollBy(0, 600);")

driver.find_element_by_css_selector("ul>li>a>h3").click()

driver.find_element_by_class_name("reviews_tab").click()

driver.find_element_by_class_name("star-5").click()

reviews = driver.find_element_by_id("comment")
reviews.send_keys("Nice book!")

email = driver.find_element_by_css_selector("form>div>p:nth-child(1)>input:nth-child(1)")
email.send_keys("sfwcds")

driver.find_element_by_id("submit")

driver.quit()

