from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
driver.maximize_window()
rows=len(driver.find_elements(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr"))
print(rows)
columns=len(driver.find_elements(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr[1]/td"))
print(columns)
for r in range(1,rows+1):
    if driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr["+str(r)+"]/td[3]")==29:
        result=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr["+str(r)+"]/td[1]")
        print(result.text)
