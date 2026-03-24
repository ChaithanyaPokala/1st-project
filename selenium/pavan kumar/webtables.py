import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# to print all rows in the table
all_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
print(all_rows)
# to print all the columns in the table
all_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
print(all_columns)
# to print the specific thing in the table

dta=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[1]").text
print(dta)
# to print all the rows and columns
# for r in range(2,all_rows+1):
#     for c in range(1,all_columns+1):
#         dta=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(dta)

# codition
for r in range(2,all_rows+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]/td[1]").text
        # print(book_name)
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]/td[4]").text
        print(book_name,"  ",price)


