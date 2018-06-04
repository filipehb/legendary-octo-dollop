from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from google import Google

options = Options()
options.add_argument('--ignore-certificate-errors')
#options.add_argument('headless')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)

google = Google(driver)
google.navigate()
