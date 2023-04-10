import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# there will be class for performing mouse operations

action = ActionChains(driver)

# action.click_and_hold("just pass the element locator")
# action.context_click("just pass the element locator")
# action.double_click("just pass the element locator")
# action.drag_and_drop("just pass the element locator")

action.move_by_offset(driver.find_element(By.ID, "mousehover")).perform()
