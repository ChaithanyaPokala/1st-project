import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='field1']").clear()
driver.find_element(By.XPATH,"//*[@id='field1']").send_keys("Chaithanya")
act=ActionChains(driver)
click=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
act.double_click(click).perform()
