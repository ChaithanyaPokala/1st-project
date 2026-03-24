import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
actual_list=["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
expected_list=[]
driver.find_element(By.XPATH,"//*[@id='root']/div/header/div/div[2]/form/input").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
name="rahulshettyacademy"
assert count>0
for result in results:
    expected_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expected_list == actual_list

driver.find_element(By.XPATH,"//*[@id='root']/div/header/div/div[3]/a[4]/img").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()
amounts=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for amount in amounts:
    sum = sum+int(amount.text)
print(sum)
price=driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/span[1]")
assert sum==int(price.text)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys(name)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/button").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
discountamount=driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/span[3]")
assert discountamount.text<price.text
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/button").click()





