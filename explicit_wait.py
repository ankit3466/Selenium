from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.maximize_window()  # for open browser in full size

driver.implicitly_wait(10)

driver.get("https://www.expedia.com")
print(driver.title)

# click on flight
driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")  # origin

time.sleep(5) # for python code

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC") # for destination

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("8/29/2019")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("9/6/2019")

driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# now time to apply explicit wait
# note that explicit wait is not concern with time . its about based on some condition
# it means that it will wait for a period untill specified condition is not satisfied

wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

element.click()
time.sleep(3)
driver.quit()
