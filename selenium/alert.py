import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name="Chaithanya"
driver.find_element(By.XPATH,"//*[@id='name']").send_keys(name)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()
time.sleep(2)
alert=driver.switch_to.alert
alerttext=alert.text
print(alerttext)
assert name in alerttext
alert.accept()


