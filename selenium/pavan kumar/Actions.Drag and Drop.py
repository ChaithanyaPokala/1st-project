import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,1000)")
source=driver.find_element(By.XPATH,"//*[@id='angular']")
target=driver.find_element(By.XPATH,"//*[@id='droparea']")
act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
