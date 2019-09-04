from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

print(driver.title)

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

# Mouse Hover action
admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]')
mang = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
user = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(mang).move_to_element(user).click().perform()