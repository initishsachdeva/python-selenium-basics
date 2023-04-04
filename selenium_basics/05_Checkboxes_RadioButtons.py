import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# ------------- Checkboxes Example -----------------
# if multiple checkboxes are there and you need to select 1 from that list

checkboxes = driver.find_elements(By.XPATH, "input[@type = 'checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# ------------ Radio Buttons - --------------

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# if you know the position of elements won't change, directly pass the index.
radioButtons[2].click()
assert radioButtons[2].is_selected()

# ------------- verify text is displayed or not --------------

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()





















