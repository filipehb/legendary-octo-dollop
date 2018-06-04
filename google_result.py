from collections import namedtuple
from selenium import webdriver

class GoogleResults:
    timer = 40

    def __init__(self, driver):
        self.driver = driver
        self.result = "//div[@class='rc']" #xpath
        self.title = self.result + "/h3" #xpath
        self.date = self.result + "//span[@class='f']" #xpath
        self.link = self.result + "//cite" #xpath
        self.descr = self.result + "//span[@class='st']" #xpath
        self.event = namedtuple('Event',
                                'title date link descr')

    def _get_news(self):
        return self.driver.find_elements_by_xpath(self.result)

    def _get_title(self, new):
        return self.new.find_element_by_xpath(self.title)

    def _get_link(self, new):
        return self.new.find_element_by_xpath(self.link)

    def _get_descr(self, new):
        return self.new.find_element_by_xpath(self.descr)

    def _get_date(self, new):
        return self.new.find_element_by_xpath(self.date)

    def get_all_data(self):
        results = self._get_news()
        for new in results:
            yield self.event(self._get_title(new).text,
                             self._get_date(new).text,
                             self._get_link(new).text,
                             self._get_descr(new).text)
