import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/selenium/practice/scroll-down.php")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
# result=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/h3[2]")
# driver.execute_script("arguments[0].scrollIntoView()",result)
# time.sleep(1)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)