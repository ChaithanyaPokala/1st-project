import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[2]")).click().perform()
