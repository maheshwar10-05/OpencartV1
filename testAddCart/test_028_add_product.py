import time

from pageOjects.Homepage import Home
from utilities.readProperties import ReadConfig


class TestCart():
    baseURL = ReadConfig.getApplicationURL()
    def test_add_to_cart(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.hp.components()
        # if self.hp.components() == "Success: You have added Apple Cinema 30 to your shopping cart!":
        #     assert True
        # else:
        #     assert False



