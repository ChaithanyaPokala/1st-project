import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()



driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am there")

time.sleep(2)
driver.switch_to.default_content()
alerts=driver.find_element(By.XPATH,"//h3").text
print(alerts)