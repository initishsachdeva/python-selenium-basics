import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# implicit wait declaration
driver.implicitly_wait(5)  # in seconds
# driver.manage().timeouts().implicitlyWait(5);

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# can be used to pause the execution of the current thread for a specified time in milliseconds.
time.sleep(2)

productsList = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
print(len(productsList))
count = len(productsList)
assert count > 0
for listItems in productsList:
    # it will add to cart first item in the list = chaining of web elements.Loop will execute 3 times will add to cart all items one by one
    listItems.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//*[text() = 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("abcdef")
driver.find_element(By.XPATH, "//*[text() = 'Apply']").click()

# ---------clicking on apply is taking some time to complete it's actions

# ----------------- Waits in Selenium -------------------------
# 2 types of wait are there - 1. Implicit wait  2. Explicit wait

# ------------------- Implicit Wait ---------------
# ---- it is like a global wait
# driver.implicitlyWait(5);  - 5 seconds is a max time it will wait ,but if it completes ops in 2 seconds it will move to next step and 3 seconds will be saved.
# The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it throws a “No Such Element Exception”.
# The default setting is 0. Once we set the time, the web driver will wait for the element for that time before throwing an exception.


# ------------------- Explicit Wait ---------------
# The Explicit Wait in Selenium is used to tell the Web Driver to wait for certain conditions (Expected Conditions) or maximum time exceeded before throwing “ElementNotVisibleException” exception.
# It is an intelligent kind of wait, but it can be applied only for specified elements. It gives better options than implicit wait as it waits for dynamically loaded Ajax elements. Once we declare explicit wait
# we have to use “ExpectedConditions”
# this will apply to the specific scenario where we have to wait for the ops to complete

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoInfo"))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
driver.close()
