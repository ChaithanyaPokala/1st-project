import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text =="India":
        country.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"
driver.find_element(By.XPATH,"//*[@id='ctl00_mainContent_rbtnl_Trip_1']").click()
ctr=select(driver.find_element(By.ID,"ctl00_mainContent_ddl_originStation1")).click()

# ctr.select_by_index(7)
#
# time.sleep(2)

