from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# navigate to mentioned url
driver.get("https://google.com")

# maximize the window
driver.maximize_window()

# to get the title
title = driver.title
print(title)

# verify the url is correct or not
print(driver.current_url)

driver.get("https://www.facebook.com/")
driver.minimize_window()

# to go back to previous URL
driver.back()

# to refresh the page
driver.refresh()

# to go forward
driver.forward()

driver.close()
