import time
import pytest
from pageOjects.Homepage import Home
from pageOjects.LoginPage import LoginPage
from utilities import ExcelUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = "C:/Users/2148389/PycharmProjects/OpenCartV1/testData/Opencart_LoginData.xlsx"
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = Home(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class

        for r in range(2, self.rows + 1):
            self.hp.clickaccount()
            self.hp.clicklogin()

            self.email = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.login_email(self.email)
            self.lp.login_password(self.password)
            self.lp.click()
            time.sleep(3)

            if self.exp == 'Valid':
                    lst_status.append('Pass')
                    self.hp.clickaccount()
                    self.hp.clicklogout()
            elif self.exp == 'Invalid':
                if self.lp.invalid_confirmation() == True:
                    lst_status.append('Fail')
                    self.hp.clickaccount()
                    self.hp.clicklogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        print(lst_status)
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
