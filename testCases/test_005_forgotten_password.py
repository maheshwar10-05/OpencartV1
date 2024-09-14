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


class Test_login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_login_page(self, setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.logger.info("clicking on Myaccount---->Login")
        self.hp.clickaccount()
        time.sleep(5)
        self.hp.clicklogin()
        self.logpage = LoginPage(self.driver)
        self.logpage.forgot_pass()
        if self.logpage.conf_forgotten() == "Forgot Your Password?":
            assert True
            self.driver.close()
        else:
            assert False






