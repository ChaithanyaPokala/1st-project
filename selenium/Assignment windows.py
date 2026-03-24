from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[1]/a[1]").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
ass_text=driver.find_element(By.XPATH,"//*[@id='interview-material-container']/div/div[2]/p[2]/strong/a").text
print(ass_text)
driver.switch_to.window(windows[0])
driver.find_element(By.XPATH,"//*[@id='username']").send_keys(ass_text)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("rahulshetty")
# driver.find_element(By.XPATH,"//*[@id='login-form']/div[4]/div/label[2]/span[2]").click()
# driver.find_element(By.XPATH,"//*[@id='login-form']/div[6]/label/span[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='signInBtn']").click()