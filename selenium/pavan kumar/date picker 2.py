import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='datepicker2']").click()
drpdwn=Select(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/select[1]"))
drpdwn.select_by_index(6)
drpdwn2=Select(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/select[2]"))
drpdwn2.select_by_index(1)
date=25
dates=driver.find_elements(By.XPATH,"//table/tbody/tr/td/a")
for ele in dates:
    if ele==date:
        ele.click()
    break

