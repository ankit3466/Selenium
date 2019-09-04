from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.maximize_window()  # for open browser in full size

driver.implicitly_wait(10)  # this will wait for 10 second to appear all the elements on the page
# this wait is applicable for all the element present on the page and this wait is not related to python code

driver.get("http://newtours.demoaut.com/")

print(driver.title)

user_ele = driver.find_element_by_name("userName")
pass_ele = driver.find_element_by_name("password")

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")
# click on login button
driver.find_element_by_name("login").click()
