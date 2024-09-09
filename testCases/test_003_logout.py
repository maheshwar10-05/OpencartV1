import os.path
import time
from selenium import webdriver
import pytest
import string
from pageOjects.Homepage import Home
from pageOjects.LoginPage import LoginPage
from pageOjects.MyAccountPage import MyAccountPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_logout():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_log_out_page(self, setup):
        self.logger.info("***Test started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.logger.info("clicking on Myaccount---->Login")
        self.hp.clickaccount()
        time.sleep(5)
        self.hp.clicklogin()
        self.logger.info("Providing Customer details fro registration")

        self.logpage = LoginPage(self.driver)
        self.logpage.login_email("itachi123456@gmail.com")
        self.logpage.login_password("Naruto@12345")
        self.logpage.click()
        self.hp.clickaccount()
        self.hp.clicklogout()
        time.sleep(3)
        self.conf_messagesd = self.logpage.login_out()
        if self.conf_messagesd == "Account Logout":
            self.logger.info("Account is successfully logged out")
            print("ok")
            assert True
        else:
            self.logger.debug()
            assert False
