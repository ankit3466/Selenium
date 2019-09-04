from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.maximize_window()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

print(driver.current_window_handle)   # this will give the current window handler

# for all tabs
tabs = driver.window_handles
print(len(driver.window_handles))

for tab in tabs:
    driver.switch_to.window(tab)
    print(driver.title)
    # for closing a specific tab
    #if driver.title == "Title Name":
     #   driver.close()

driver.quit()