from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
rows=len(driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr"))
print(rows)
columns=len(driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr[1]/td"))
print(columns)
ans = []
# mini = float('inf')
for r in range(1,rows+1):
    result=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(r)+"]/td[4]").text
    print(result)
    ans.append(float(result[:-1]))
    print(driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(r)+"]/td[1]").text)
    # mini = min(mini,float(result[:-1]))
print(ans)
print(min(ans))
print(driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(r)+"]/td[1]").text)