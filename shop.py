################## Первое задание:отображение страницы товара

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
driver.maximize_window()

my_account_menu = driver.find_element_by_link_text("My Account").click()
user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardPassword123!@#!@#")
login_btn =driver.find_element_by_name("login").click()
#Переход на вкладку "Shop"
#shop_tab =driver.find_element_by_link_text('Shop')
shop_tab = driver.find_element_by_id("menu-item-40").click()

html5_forms =driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]').click()

#product_title = driver.find_element_by_css_selector('h1.product_title.entry-title')

product_title_check = driver.find_element_by_css_selector('h1.product_title.entry-title')
product_title_check = product_title_check.text
assert "HTML5 Forms" in product_title_check

driver.quit()

################## второе задание: количество товаров в категории


import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
driver.maximize_window()

my_account_menu = driver.find_element_by_link_text("My Account").click()
user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardPassword123!@#!@#")
login_btn =driver.find_element_by_name("login").click()
#Переход на вкладку "Shop"
#shop_tab =driver.find_element_by_link_text('Shop')
shop_tab = driver.find_element_by_id("menu-item-40").click()

html = driver.find_element_by_css_selector(".cat-item.cat-item-19  >a").click()
items_count = driver.find_elements_by_css_selector('.woocommerce-LoopProduct-link h3')

if len(items_count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка. Количество товаров : " + str(len(items_count)))

driver.quit()

 ############## Третье задание: сортировка товаров

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

my_account_menu = driver.find_element_by_link_text("My Account").click()
user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardPassword123!@#!@#")
login_btn = driver.find_element_by_name("login").click()
# Переход на вкладку "Shop"
# shop_tab =driver.find_element_by_link_text('Shop')
shop_tab = driver.find_element_by_id("menu-item-40").click()

from selenium.webdriver.support.select import Select
selector =driver.find_element_by_css_selector("select.orderby")
selector_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"select.orderby"),"Default sorting"))
if selector_check is not None:
    print("Выбран вариант по умолчанию")

select = Select(selector)
select.select_by_value("price-desc")
selector_high = driver.find_element_by_css_selector("select.orderby")
selector_high_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"select.orderby"),"Sort by price: high to low"))
if selector_high is not None:
    print("Выбрана сортировка от большей цены к меньшей")

driver.quit()

############### Четвёртое задание: отображение, скидка товара

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

my_account_menu = driver.find_element_by_link_text("My Account").click()
user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardPassword123!@#!@#")
login_btn = driver.find_element_by_name("login").click()
# Переход на вкладку "Shop"
# shop_tab =driver.find_element_by_link_text('Shop')
shop_tab = driver.find_element_by_id("menu-item-40").click()

#Открытие папки Андроид Квик Старт Гайд
android_quick_start_book =driver.find_element_by_css_selector(".post-169 h3").click()
#android_quick_start_book=driver.find_element_by_css_selector("post-169 > a.nth-child(1)")

#Получение значения новой и старой цены
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text =book_old_price.text
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text

#Проверка значений цен
assert book_old_price_text == "₹600.00"
assert book_new_price_text == "₹450.00"

#Явное ожидание для обложки книги
book_cover = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))).click()
#book_cover.click

#Явное ожидание для кнопки закрытия обложки книги в режиме предпросмотра
book_cover_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
time.sleep(2)
book_cover_close.click()
driver.quit()

################# Пятое задание: проверка цены в корзине

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

shop_tab = driver.find_element_by_id("menu-item-40").click()
add_to_cart = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop").click()

# Проверка количества товаров в корзине
basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
basket_item_value_text = basket_item_value.text
assert basket_item_value_text == "1 Item"
# Проверка стоимости товаров в корзине
basket_price_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
basket_price_value_text = basket_price_value.text
assert basket_price_value_text == "₹180.00"

busket = driver.find_element_by_css_selector('[title = "View your shopping cart"]').click()


subtotal_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td"),"₹180.00"))
total_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"tr.order-total >td"), "₹189.00"))

driver.quit()

######### Шестое задание: Shop: работа в корзине

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.maximize_window()
shop_tab = driver.find_element_by_id("menu-item-40").click()

driver.execute_script("window.scrollBy(0, 300);")

add_to_cart_html = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
add_to_cart_js = driver.find_element_by_css_selector('[data-product_id="180"]').click()

busket = driver.find_element_by_css_selector('[title = "View your shopping cart"]').click()

time.sleep(1)

remove_html = driver.find_element_by_css_selector('a.remove[data-product_id="182"]').click()
undo =driver.find_element_by_css_selector("div.woocommerce-message >a").click()

clear_html = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]").clear()


add_html = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]") #Добавление 3 книг в корзину
add_html.send_keys("3")
update_basket = driver.find_element_by_css_selector('input.button[name="update_cart"]').click()

html_quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]") #проверка количества книг
html_quantity_check = html_quantity.get_attribute("value")
assert html_quantity_check == "3"
time.sleep(1)

apply_coupon =driver.find_element_by_css_selector('input.button[name="apply_coupon"]').click()

error = driver.find_element_by_css_selector("ul.woocommerce-error")
error_text = error.text
if error_text == "Please enter a coupon code.":
    print('Сообщение об ошибке появилось')
else:
    print('Сообщение об ошибке не появилось')

driver.quit()

######### Седьмое задание: Shop: покупка товара

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.maximize_window()
shop_tab = driver.find_element_by_id("menu-item-40").click()

driver.execute_script("window.scrollBy(0, 300);")

add_to_cart_html = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
busket = driver.find_element_by_css_selector('[title = "View your shopping cart"]').click()


proceed_to_checkout = driver.find_element_by_css_selector("a.checkout-button.button.alt.wc-forward")
proceed_to_checkout_check = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button.button.alt.wc-forward")))
proceed_to_checkout.click()

first_name = driver.find_element_by_css_selector("input#billing_first_name.input-text")
first_name_check = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#billing_first_name.input-text" )))
first_name.send_keys("Vakhtang")

last_name = driver.find_element_by_css_selector("input#billing_last_name.input-text")
last_name.send_keys("Makharadze")

email = driver.find_element_by_css_selector("input#billing_email.input-text")
email.send_keys("spam@yourself.com")

phone = driver.find_element_by_css_selector("input#billing_phone.input-text")
phone.send_keys("+79261113366")


driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

country_select = driver.find_element_by_css_selector("span.select2-arrow").click()
country = driver.find_element_by_css_selector("#s2id_autogen1_search")
country.send_keys("Russia")
country_click =driver.find_element_by_css_selector("span.select2-match").click()

address = driver.find_element_by_css_selector("input#billing_address_1.input-text")
address.send_keys("Alekseevskaya 4-1-4")

city = driver.find_element_by_css_selector("input#billing_city.input-text")
city.send_keys("Moscow")

state = driver.find_element_by_css_selector("input#billing_state.input-text")
state.send_keys("Russia")

postcode = driver.find_element_by_css_selector("input#billing_postcode.input-text")
postcode.send_keys("454000")

driver.execute_script("window.scrollBy(0, 600);")

check_payment = driver.find_element_by_css_selector("input#payment_method_cheque.input-radio").click()

place_order = driver.find_element_by_css_selector("input#place_order.button.alt").click()

thank_you = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"p.woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))

check_payment = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"li.method"),"Check Payments"))

driver.quit()











