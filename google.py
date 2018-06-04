from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Google:
    timer = 40

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com.br'
        self.search_bar = 'lst-ib' #id
        self.btn_search = 'btnK' #name
        self.btn_next = 'pnnext' #id

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).click()
        WebDriverWait(driver, timer).until(
            lambda driver: self.driver.find_element_by_id(self.btn_next))
