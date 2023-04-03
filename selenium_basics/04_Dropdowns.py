import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# -------------- Static Dropdown -----------------------
# We handle dropdown in Selenium using SELECT Class


dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

# 1. By Text = this will select value based on the text matched in the dropdown
dropdown.select_by_visible_text("Female")

# 2. By Index = this will select value based on the index for eg if we have 5 values and need to select first then pass index as 0.

dropdown.deselect_by_index(0)

# 3. By Value
# dropdown.select_by_value()

driver.close()

# -------------- Auto suggestive/dynamic Dropdown -----------------------
#
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)  # script will wait for 2 seconds
# for dynamic dropdowns use for loops as when you pass partial text it will show multiple matching options.
# so you have to dynamically select the option from the drodown
countries = driver.find_elements(By.CSS_SELECTOR, "li[class*='ui-menu-item']")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

# will show whether items got selected or not = use getattribute method when you update value through scripts for dynamic dropdowns
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
