from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Frames are like different portions of a webpage . Just like they depend on each other. On clicking a element of a frame will gives diff. options in another frame and so on.
driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

# first to switch to 1 frame
# 2 method by name or id
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

# Now we are in 1 frame we need to come back to the main frame so that we can jump to the next frame
driver.switch_to.default_content()

# second frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Capabilities").click()
time.sleep(3)

driver.switch_to.default_content()

# third frame
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)

driver.close()