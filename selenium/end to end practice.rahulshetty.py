import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Chaithanya")
# driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("chaithu@gmail.com")
# driver.find_element(By.XPATH,"//*[@id='exampleInputPassword1']").send_keys("Chaithu@143")
# drp_dwn=Select(driver.find_element(By.XPATH,"//*[@id='exampleFormControlSelect1']"))
# drp_dwn.select_by_index(1)
# driver.find_element(By.XPATH,"//*[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()
# driver.execute_script("window.scrollTo(0, 500);")
mobiles=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
# time.sleep(5)
for mobile in mobiles:
    mobile_name=mobile.find_element(By.XPATH,"div/h4/a").text
    print(mobile_name)
    if mobile_name=="Blackberry":
        # time.sleep(5)
        mobile.find_element(By.XPATH,"div/button").click()
        # time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li/a").click()
driver.find_element(By.XPATH,"//button[@Class='btn btn-success']").click()
driver.find_element(By.XPATH,"//*[@id='country']").send_keys("ind")
countries=driver.find_elements(By.XPATH,"//ul/li/a")
for country in countries:
    if country.text=="India":
        time.sleep(5)
        country.click()
        time.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div[1]/div[2]").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
result=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you" in result
driver.close()























