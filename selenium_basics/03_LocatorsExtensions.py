from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password").click()

# traversing from Parent to child by using xpaths

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("abc@gmail.com")

driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("abc")

# in CSS for parent to child traversing give space in bw

driver.find_element(By.XPATH, "form div:nth-child(3) input").send_keys("abc")

# write xpaths just by using the text displayed on UI
driver.find_element(By.XPATH, "//button[text()= 'Save New Password']").click()

driver.close()
