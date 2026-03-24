import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/")
driver.maximize_window()
# driver.execute_script("window.scrollBy(0,3000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
canada=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[38]/td[2]/a")
driver.execute_script("arguments[0].scrollIntoView()",canada)








# driver.get_screenshot_as_file(filename="screenshot.png")