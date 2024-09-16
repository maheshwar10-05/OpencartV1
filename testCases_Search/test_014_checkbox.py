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

class Test_Criteria():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_search_criteria(self,setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_button()
        self.srch.criteria("iLife")
        self.srch.check_box()
        self.srch.btn_src()
        self.srch.desc_text()
        if "iLife" in self.srch.desc_text():
            assert True
        else:
            assert False
