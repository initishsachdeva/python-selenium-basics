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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

# selenium doesn't provide support for scrolling down the page but it can support using javascript

# it will scroll down to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# to get the screenshot
driver.get_screenshot_as_file("screen.png")
driver.save_screenshot()