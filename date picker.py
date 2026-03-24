import time
from tokenize import maybe

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='datepicker1']").click()
month="May"
Date="25"
year="2001"
mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
yea=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
while True:
    if month==mon and year==yea:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()
        mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        yea = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

dates=driver.find_elements(By.XPATH,"//table[@class= 'ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text==Date:
        date.click()
    break















