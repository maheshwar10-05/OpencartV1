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

class Test_loginsearch():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_login_search(self,setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.hp.clickaccount()
        self.hp.clicklogin()
        self.logpage = LoginPage(self.driver)
        self.logpage.login_email("itachi123456@gmail.com")
        self.logpage.login_password("Naruto@12345")
        self.logpage.click()
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        if self.srch.product_dis() == "iMac":
            assert True
        else:
            assert False
        self.driver.close()