from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="C:/Driver/Firefox/geckodriver")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# selecting values
drp.select_by_index(2)
 #drp.select_by_visible_text("Morning")
 #drp.select_by_value("Radio-1")

# count the options
print(len(drp.options))

# capture all options
all_option = drp.options

for op in all_option:
    # print(op)  this will return selenium object
    print(op.text)
    print('\n')


#driver.close()