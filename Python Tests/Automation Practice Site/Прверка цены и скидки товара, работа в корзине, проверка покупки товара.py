from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_1'
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

driver.find_element_by_link_text("Shop").click()

driver.find_element_by_css_selector(".products.masonry-done>.post-169").click()

old_price = driver.find_element_by_css_selector(".price > del > span") # нашли элемент по составному селектору
old_price_text = old_price.text # получили текст элемента с помощью .text
assert old_price_text == "₹600.00" # добавили проверку что содержимое равно ожидаемому

new_price = driver.find_element_by_css_selector(".price > ins > span") # нашли элемент по составному селектору
new_price_text = new_price.text # получили текст элемента с помощью .text
assert new_price_text  == "₹450.00" # добавили проверку что содержимое равно ожидаемому

book_img = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single")) )
book_img.click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) ).click()
driver.quit()

#######################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

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

driver.find_element_by_link_text("Shop").click()

element = driver.find_element_by_css_selector(".post-181>.woocommerce-LoopProduct-link>h3") # нашли элемент по составному селектору
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "HTML5 Forms" # добавили проверку что содержимое равно ожидаемому
driver.quit()

#######################################################################################################################3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

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

driver.find_element_by_link_text("Shop").click()

driver.find_element_by_css_selector(".cat-item-19>a").click()

print(len(driver.find_elements_by_class_name("woocommerce-LoopProduct-link")))

driver.quit()

####################################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

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

driver.find_element_by_link_text("Shop").click()

driver.find_element_by_css_selector(".products.masonry-done>.post-182>.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()

element = driver.find_element_by_class_name("wpmenucart-contents>.amount") # нашли элемент по составному селектору
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "₹180.00" # добавили проверку что содержимое равно ожидаемому

element = driver.find_element_by_css_selector(".wpmenucartli>.wpmenucart-contents>.cartcontents") # нашли элемент по составному селектору
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "1 item"

driver.quit()

################################################################################################################3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

path_to_extension = r'C:\Users\Наталья\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

driver.maximize_window()
driver.implicitly_wait(5)# говорим WebDriver искать каждый элемент в течение 5 секунд
wait = WebDriverWait (driver, 10)
driver.get("https://practice.automationtesting.in//")

driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")

driver.find_element_by_css_selector(".products.masonry-done>.post-182>.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()

time.sleep(3)

driver.find_element_by_css_selector(".post-165>.product_type_simple").click()

driver.find_element_by_class_name("cartcontents").click()

time.sleep(3)

driver.find_element_by_css_selector(".cart_item:nth-child(1)>.product-remove:nth-child(1)>a").click()

driver.find_element_by_link_text("Undo?").click()

driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]").clear()
quantity = driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]")
quantity.send_keys("3")

driver.find_element_by_name("update_cart").click()

# element = driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]") # нашли элемент
# element_get_text = element.text # получили текст элемента с помощью .text
# assert element_get_text == "3" # добавили проверку что содержимое равно ожидаемому

time.sleep(3)

driver.find_element_by_name("apply_coupon").click()

element = driver.find_element_by_css_selector(".woocommerce-error>li")
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "Please enter a coupon code." # добавили проверку что содержимое равно ожидаемому

driver.quit()

######################################################################################################################

import time
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

driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")

driver.find_element_by_css_selector(".products.masonry-done>.post-182>.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()

driver.find_element_by_class_name("added_to_cart.wc-forward").click()

btn = WebDriverWait(driver, 10).until( # говорим Selenium проверять в течение 10 секунд, пока кнопка не станет кликабельной
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward")) )
btn.click()

first_name = driver.find_element_by_id("billing_first_name")
first_name .send_keys("dfcadfcs")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("edfedfvdcwsedcwf")

email = driver.find_element_by_id("billing_email")
email.send_keys("tusya1096@gmail.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("4534656346463")

driver.find_element_by_id("s2id_billing_country").click()
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
driver.find_element_by_id("select2-results-1").click()

add = driver.find_element_by_id("billing_address_1")
add.send_keys("dgvdfvdfv45")

city = driver.find_element_by_id("billing_city")
city.send_keys("Dfsddf")

city = driver.find_element_by_id("billing_state")
city.send_keys("Dgdfgbdfbdfbdf")

post = driver.find_element_by_id("billing_postcode")
post.send_keys("ASqwdwdd")

driver.execute_script("window.scrollBy(0, 600);")

time.sleep(3)

driver.find_element_by_id("payment_method_cheque").click()

driver.find_element_by_id("place_order").click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

some_element1= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)"), "Check Payments"))

driver.quit()





