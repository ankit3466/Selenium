from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element = driver.find_element_by_xpath('//*[@id="box7"]')
target_element = driver.find_element_by_xpath('//*[@id="box107"]')

action = ActionChains(driver)

action.drag_and_drop(source_element,target_element).perform()
