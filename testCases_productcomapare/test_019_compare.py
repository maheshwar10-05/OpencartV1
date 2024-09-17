import pytest

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageOjects.Search import Search


class Test_Compare():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_compare(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        self.srch.img_link()
        self.validate = self.srch.hover_move()
        if self.validate == ("Success: You have added iMac to your product comparison! ×"):
            assert True
        self.link = self.srch.product_link_detail()
        if self.link == "Product Details":
            assert True
        else:
            assert False
