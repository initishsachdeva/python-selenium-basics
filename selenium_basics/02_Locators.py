from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# --------------- Different Types of Locators are --------------
# ---------- ID, Xpath , CSS Selector,  Classname , name, LinkText

driver.find_element(By.NAME, "name").send_keys("Demo")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# constructing xpaths = //tagname[@attribute = "value"]
# constructing css = tagname[attribute = "value"] - > "input[type = 'submit' , in css for id = # id and for class = .className ]"

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

driver.find_element(By.XPATH, "//input[@type = 'submit' ]").click()

# text method will grab the text from UI
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# if the elements returned are more than 1, than you can mention the index of matching elemt you want
driver.find_element(By.XPATH, "input[@type = 'text'])[3]").send_keys("dummy description")

# clear method will clear the text from input field
driver.find_element(By.XPATH, "input[@type = 'text'])[3]").clear()

driver.close()
