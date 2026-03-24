from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='txt1']")))
driver.find_element(By.XPATH,"//*[@id='txt1']").send_keys("Chaithanya")