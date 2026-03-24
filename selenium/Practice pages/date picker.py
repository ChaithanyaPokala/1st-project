import time
from tokenize import maybe

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='datetimepicker1']").click()
drpdwn=Select(driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/select"))
drpdwn.select_by_index(2)
time.sleep(5)
year="2001"
date="25"
yea=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/input").get_attribute("value")
while True:
    if yea==year:
        break
    else:

        driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/span[2]").click()
        yea=driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/input").get_attribute("value")

dates=driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/span")
for dat in dates:
    if dat==date:
        dat.click()
time.sleep(5)




