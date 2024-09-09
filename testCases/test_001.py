import os.path
import time
from selenium import webdriver
import pytest
import string
from pageOjects.Homepage import Home
from pageOjects.Accountregistrationpage import Register
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Register():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_register(self, setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.logger.info("clicking on Myaccount---->Register")
        self.hp.clickaccount()
        time.sleep(5)
        self.hp.clickregister()
        self.logger.info("Providing Customer details fro registration")
        self.regpage = Register(self.driver)
        self.regpage.setFirstname("naruto")
        self.regpage.setLastname("uzumakhi")
        self.email = randomString.random_string_generator() + "@gmail.com"
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("itachi123456@gmail.com")
        self.regpage.setTelephone("9876543908")
        self.regpage.setPassword("Naruto@12345")
        self.regpage.setConfirmPassword("Naruto@12345")
        self.regpage.txtsub()
        self.regpage.txtpol()
        self.regpage.clickbutton()
        time.sleep(3)
        self.text = self.regpage.conf()
        if self.text == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Account registration is failed")
            self.driver.save_screenshot(
                "C:/Users/2148389/PycharmProjects/OpenCartV1" + "\\screenshots\\" + "accountreg.png")
            self.driver.quit()
            print("not ok")
