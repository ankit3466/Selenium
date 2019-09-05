from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("http://newtours.demoaut.com/")

print(driver.title)

# getting user and pass field
user_ele = driver.find_element_by_name("userName")
pass_ele = driver.find_element_by_name("password")

# ensuring these field
print(user_ele.is_displayed())
print(user_ele.is_enabled())

print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

# sending data to these field
user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

# click on login button
driver.find_element_by_name("login").click()

#time.sleep(20)

rt=driver.find_element_by_css_selector("input[value=roundtrip]")
print(rt.is_selected())

ow=driver.find_elements_by_css_selector("input[value=oneway]")
print(ow.is_selected())