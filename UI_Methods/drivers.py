from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class drivers:

    def get_chrome_driver(self, driver_location):
        driver = webdriver.Chrome("{0}".format(driver_location))
        return driver