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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5)

browserSortedLIst = []
# ---------------- how to sort web tables -------------------------
# we have below use case
# 1. click on column header

driver.find_element(By.XPATH, "//span[@text() = 'Veg/fruit name']").click()

# 2. collect all names from first row column

firstRowList = driver.find_elements(By.XPATH, "//tr/td[1]")
for elements in firstRowList:
    browserSortedLIst.append(elements.text)

originalListSortedByBrowser = browserSortedLIst.copy()
# 3. sort the list into new sorted list

browserSortedLIst.sort()

# compare both the list and that should match
assert browserSortedLIst == originalListSortedByBrowser
