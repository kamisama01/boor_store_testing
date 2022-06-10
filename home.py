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

driver.execute_script("window.scrollBy(0, 600);")

book =driver.find_element_by_css_selector('[alt="Selenium Ruby"]').click()
review = driver.find_element_by_css_selector("ul.tabs.wc-tabs :nth-child(2)").click()
star = driver.find_element_by_class_name("star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice Book!")

name = driver.find_element_by_id("author")
name.send_keys("Vakhtang")
email =driver.find_element_by_id("email")
email.send_keys("spam@yourself.com")
submit =driver.find_element_by_id("submit").click()