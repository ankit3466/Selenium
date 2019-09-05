from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

# Navigation ----like go forwaor and come back
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

print(driver.title)

# for come back
driver.back()

print(driver.title)

# for go forward
driver.forward()

print(driver.title)
driver.close()