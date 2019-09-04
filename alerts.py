from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)

# clicking for alert popup
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(3)
# switching to alert window then click
# by press ok button
driver.switch_to_alert().accept()

# by click on cancle button
driver.switch_to_alert().dismiss()

time.sleep(3)
driver.close()