from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

action = ActionChains(driver)

action.context_click(button).perform()   # Right click perform