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
from pageOjects.ForgottenpasswordPage import EnterMail


class Test_mail():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_forgottenpassword_page(self, setup):
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
        self.fp = EnterMail(self.driver)
        self.fp.forgot_email_enter("itachi123456@gmail.com")
        self.fp.click_continue()
        if self.fp.link_sent() == "An email with a confirmation link has been sent your email address.":
            assert True
        else:
            assert False