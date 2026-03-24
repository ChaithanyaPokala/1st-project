from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='content']/div/a").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
new_wind_text=driver.find_element(By.XPATH,"/html/body/div/h3").text
print(new_wind_text)
assert "New Window" == new_wind_text
driver.switch_to.window(windows[0])
old_wind_text=driver.find_element(By.XPATH,"//*[@id='content']/div/h3").text
print(old_wind_text)
assert "Opening a new window"==old_wind_text



