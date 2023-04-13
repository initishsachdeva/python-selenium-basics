from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ------------ chrome options available are ------------

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# to open window in specific resolution
chrome_options.add_argument("window-size=1920*1080")

# Chrome Driver
# provide the chrome drive path located in your system
service_obj = Service("C:/Users/nitsachdeva/PycharmProjects/chrome-drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
