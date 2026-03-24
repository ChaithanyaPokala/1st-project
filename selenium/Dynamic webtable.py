import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.livecoinwatch.com/")
driver.maximize_window()
rows=len(driver.find_elements(By.XPATH,"//table[@class='lcw-table layout-fixed']/tbody/tr/td[8]/span"))
print(rows)
for r in range(2,rows+1):
    coins=driver.find_element(By.XPATH,"//table[@class='lcw-table layout-fixed']/tbody/tr["+str(r)+"]/td[8]/span").text
    cleaned_coins=coins.replace('%','')
    coin_value=float(cleaned_coins)
    if coin_value > 0.04:
        # print(coin_value)
        result=driver.find_element(By.XPATH,"//table[@class='lcw-table layout-fixed']/tbody/tr["+str(r)+"]/td[2]").text
        print(result)



    # coins = '2.3%'      to avoid % in the last one
    # coins = coins[:-1]
         # print(driver.find_element(By.XPATH,"//table[@class='lcw-table layout-fixed']/tbody/tr["+str(r)+"]/td[2]")).text



