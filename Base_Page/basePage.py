import sys
from selenium import webdriver


class Page(object):
    driver = webdriver.Chrome
    '''
        page基类
    '''

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        pass

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
        pass

    def input(self, loc, text):
        self.find_element(*loc).send_keys(text)
        pass

    def click(self, loc):
        self.find_element(*loc).click()

    def get_messg(self, loc):
        return self.find_element(*loc).text

    def get_title(self):
        return self.driver.title

