from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# three methods of scrolling
# scrolling uses java methods

# 1. to a specified pixles
driver.execute_script("windows.scrollBy(0,1000)","")

# 2. to end of the page
driver.execute_script("windows.scrollBy(0,document.body.scrollHeight)")

# 3. to a element
ele = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("argument[0].scrollIntoView():",ele)

driver.close()