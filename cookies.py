from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://www.amazon.in/")

# capture cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# adding cookies
cooki = {'name':'Mycooki','value':'123'}
driver.add_cookie(cooki)

# capture cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# delete cookies
driver.delete_cookie("Mycooki")

# capture cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# delete all cookies
driver.delete_all_cookies()

# capture cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
