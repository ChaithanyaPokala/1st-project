import time
from tokenize import maybe

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
result=driver.find_element(By.XPATH,"/html/frameset/frame[1]")
driver.switch_to.frame(result)
driver.find_element(By.XPATH,"//input[@name='mytext1']").send_keys("CHAITHANYA")


