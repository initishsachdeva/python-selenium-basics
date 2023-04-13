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
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/frames")

driver.find_element(By.LINK_TEXT, "iframe").click()

# for switching to frames
driver.switch_to.frame("mce_0_fr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("i am able to switch to frames")

# to switch back to default content
driver.switch_to.default_content()
