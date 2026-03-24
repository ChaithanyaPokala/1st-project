import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.implicitly_wait(5)
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
driver.switch_to.frame("frm1")
drp=Select(driver.find_element(By.XPATH,"//*[@id='selectnav1']"))
drp.select_by_index(2)
driver.switch_to.default_content()
driver.switch_to.frame("frm2")
driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("Chaithanya")