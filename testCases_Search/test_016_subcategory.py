import os.path
import time
from selenium import webdriver
import pytest
import string
import time
from pageOjects.Homepage import Home
from pageOjects.LoginPage import LoginPage
from pageOjects.Search import Search
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SubCategory():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_search_sub_category(self,setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_button()
        self.srch.criteria("iMac")
        self.srch.sub_category()
        self.srch.btn_src()
        if self.srch.non_existing() == "There is no product that matches the search criteria.":
            assert True
        else:
            assert False
        time.sleep(5)
        self.srch.sub_check_box()
        self.srch.btn_src()
        if self.srch.product_dis() == "iMac":
            assert True
        else:
            assert False
        self.driver.close()

