import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')


driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

#my_account = driver.find_element_by_id("li#menu-item-50 > a").click()
my_account = driver.find_element_by_link_text("My Account").click()

reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("vacha@mail.ru")

reg_password = driver.find_element_by_id("reg_password")
time.sleep(2)
reg_password.send_keys("BeTester363591#")

password_check = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.woocommerce-password-strength.good")))

submit_reg = driver.find_element_by_css_selector('[value="Register"]').click()

driver.quit()



##################### Задание 2 #####################

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')


driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account").click()

email = driver.find_element_by_id("username")
email.send_keys("vacha@mail.ru")

password = driver.find_element_by_id("password")
time.sleep(2)
password.send_keys("BeTester363591#")
login = driver.find_element_by_css_selector('[value="Login"]').click()

logout_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
if logout_check is not None:
    print("Logout доступен")
else:
    print("Logout недоступен")

driver.quit()





