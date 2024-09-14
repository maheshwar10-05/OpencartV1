import os.path
import time
from selenium import webdriver
import pytest
import string
import time
from pageOjects.Homepage import Home
from pageOjects.LoginPage import LoginPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_search():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_search(self,setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.hp.search_existing("Samsung Galaxy Tab 10.1")
        self.hp.search_button()
        if self.hp.product_dis() == "Samsung Galaxy Tab 10.1":
            assert True
        else:
            assert False
        self.driver.close()
