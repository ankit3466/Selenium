from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

# for click on button
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

#driver.close() # this will close only the current tab

# for close completely
driver.quit()