import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/practice-project")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Chaithanya")
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("Chaithanya@gmail.com")
driver.find_element(By.XPATH,"//*[@id='agreeTerms']").click()
driver.find_element(By.XPATH,"//*[@id='form-submit']").click()
time.sleep(2)


