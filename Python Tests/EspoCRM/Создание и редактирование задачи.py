import time
from selenium import webdriver # импортируем webdriver

driver = webdriver.Chrome() # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.get("https://demo.us.espocrm.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(10) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться

driver.find_element_by_id("field-language").click()
driver.find_element_by_css_selector("[value=en_GB]").click()

login_btn = driver.find_element_by_id("btn-login")
login_btn.click()
time.sleep(10)

advanced = driver.find_element_by_id("nav-tab-group-group-8")
advanced.click()

driver.find_element_by_link_text("Activities").click()
driver.find_element_by_link_text("Tasks").click()
time.sleep(10)
driver.find_element_by_class_name("filters-label").click()
driver.find_element_by_css_selector("li.checkbox:nth-child(11)").click()
time.sleep(5)
driver.find_element_by_class_name("select-all").click()
actions = driver.find_element_by_class_name("btn-group.actions")
actions.click()
driver.find_element_by_link_text("Mass Update").click()
time.sleep(5)
update = driver.find_elements_by_class_name("btn-xs-wide.action.radius-left.radius-right")
if update is None :
    print("Недоступна для выбора")
driver.find_element_by_class_name("close").click()
time.sleep(5)
driver.find_element_by_class_name("radius-left.radius-right").click()
time.sleep(7)
name = driver.find_element_by_xpath('//input[@data-name="name"]')
name.send_keys("Test")
driver.find_element_by_css_selector(".col-sm-6:nth-child(1) select").click()
driver.find_element_by_css_selector("[value=Started]").click()
driver.find_element_by_css_selector(".btn-xs-wide:nth-child(1)").click()
time.sleep(7)
driver.find_element_by_link_text("Tasks").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body[@class='has-navbar']/div[@id='content']/div[@id='main']/div[@class='list-container']/div[@class='list']/table[@class='table']/tbody/tr[@class='list-row'][1]/td[@class='cell'][1]/span[@class='record-checkbox-container']/input[@class='record-checkbox']").click()
time.sleep(5)
actions = driver.find_element_by_class_name("btn-group.actions")
actions.click()
driver.find_element_by_link_text("Remove").click()
driver.quit()
