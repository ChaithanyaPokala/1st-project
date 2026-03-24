import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxs:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        break
time.sleep(2)
driver.close()
