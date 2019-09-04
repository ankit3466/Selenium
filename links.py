from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("http://newtours.demoaut.com/")

# getting links
print(len(driver.find_elements(By.TAG_NAME,"a")))

# printing all links
links = driver.find_elements(By.TAG_NAME,"a")   # note that its find_elements not element
for link in links:
    print(link.text)

# clicking on a link 2 methods
driver.find_element(By.LINK_TEXT,"REGISTER").click()  # by giving full name
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()  # giving partial name

time.sleep(5)
driver.close()

