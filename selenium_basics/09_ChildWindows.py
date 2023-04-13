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

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowOpen = driver.window_handles  # will return the name of window in the list which are opened

# after clicking, it will switch to new window
# to switch to new window, you need to use switch to method and provide new window name

driver.switch_to.window(windowOpen[1])

print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

# to switch back to parent window
driver.switch_to.window(windowOpen[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
