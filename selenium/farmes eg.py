import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[7]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("chaithanya")
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("Chaithanya.email.com")
driver.find_element(By.XPATH,"//*[@id='form-submit']").click()