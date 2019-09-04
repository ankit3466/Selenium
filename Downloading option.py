from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# the second module will help to change the directory of Downloaded file
# By default downloaded file go in Download folder specified in chrome setting

chrom_option = Options()
chrom_option.add_experimental_option("prefs",{"download.default_directory" : "C:\Download"})

driver = webdriver.Chrome(executable_path='C:/Driver/chrome/chromedriver',chrome_options=chrom_option)

driver.get("http://demo.automationtesting.in/FileDownload.html")

# Download text file on webpage
driver.find_element_by_id("textbox").send_keys(" HELLO OK")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# Download pdf
driver.find_element_by_id("pdfbox").send_keys("PDf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

