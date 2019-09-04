from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://testautomationpractice.blogspot.com/")

# one method
driver.save_screenshot("C:/Users/user/Downloads/sc.jpg")

# another method
#driver.get_screenshot_as_file("C:/Users/user/Downloads/sc.jpg")

driver.close()