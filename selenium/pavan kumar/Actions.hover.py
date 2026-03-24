import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
but=driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/button")
but2=driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/div/a[2]")
act=ActionChains(driver)
time.sleep(2)
act.move_to_element(but).move_to_element(but2).click().perform()
