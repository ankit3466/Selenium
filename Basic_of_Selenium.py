from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("https://www.seleniumhq.org/projects/")

print(driver.title)
print(driver.current_url)

print(driver.page_source)

driver.close()
