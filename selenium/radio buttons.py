import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobutton=driver.find_element(By.XPATH,"//*[@id='radio-btn-example']/fieldset/label[2]/input")
radiobutton.click()
assert radiobutton.is_selected()

