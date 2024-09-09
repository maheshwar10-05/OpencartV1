import os.path
import time
from selenium import webdriver
import pytest
import string
import time
from pageOjects.Homepage import Home
from pageOjects.LoginPage import LoginPage
from pageOjects.MyAccountPage import MyAccountPage
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
        self.logger.info("Providing Customer details fro registration")
        self.logpage = LoginPage(self.driver)
        self.logpage.login_email("itachi123456@gmail.com")
        self.logpage.login_password("Naruto@12345")
        self.logpage.click()
        self.confirmation_message = self.logpage.confirmation()
        if self.confirmation_message == "My Account":
            self.logger.info("Account Login is passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Account Login is failed")
            self.driver.save_screenshot(
                "C:/Users/2148389/PycharmProjects/OpenCartV1" + "\\screenshots\\" + "accountreg.png")
            self.driver.quit()





