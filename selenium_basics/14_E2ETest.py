from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver
# provide the chrome drive path located in your system

service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "a[href* = 'shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class* = 'btn-primary']").click()
driver.find_element(By.XPATH, "//*[@class* = 'btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
assert "Success! Thank you" in driver.find_element(By.CLASS_NAME, "alert-success").text
driver.close()
