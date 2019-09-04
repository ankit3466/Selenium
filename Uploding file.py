from selenium import webdriver
#from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
driver.switch_to_frame(0)

driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C://Users/user/Downloads/dog.jpg")
