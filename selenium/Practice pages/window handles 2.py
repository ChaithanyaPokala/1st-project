import time
from tokenize import maybe

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#newTabBtn").click()
windows=driver.window_handles
print(windows)
driver.switch_to.window(windows[1])
driver.find_element(By.XPATH,"//*[@id='alertBox']").click()
