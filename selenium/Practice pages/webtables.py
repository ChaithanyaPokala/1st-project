import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
all_rows=len(driver.find_elements(By.XPATH,"//table[@class='table-display']/tbody/tr"))
all_columns=len(driver.find_elements(By.XPATH,"//table[@class='table-display']/tbody/tr[2]/td"))
for r in range(1,all_rows+1):
    result=driver.find_element(By.XPATH,"//table[@class='table-display']/tbody/tr[2]/td[3]").text
    print(result)
    assert result=="30"


