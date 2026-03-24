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
driver.find_element(By.XPATH,"//*[@id='newWindowBtn']").click()
driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("Chaithanya")
# parent=driver.current_window_handle
# childs=driver.window_handles
# print(parent)
# print(childs)
# for child in childs:
#     if child!=parent:
#         driver.switch_to.window(child)
#         driver.maximize_window()
#         time.sleep(1)
# driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("Chaithanya")









