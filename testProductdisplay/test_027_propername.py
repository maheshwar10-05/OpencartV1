import time

from pageOjects.ProductsDisplay import Display
from pageOjects.Search import Search
from utilities.readProperties import ReadConfig


class TestProper():
    baseURL = ReadConfig.getApplicationURL()

    def test_proper_product(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.dp = Display(self.driver)
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        self.dp.img_link()
        if self.dp.list_product_name() == ["Brand: Apple","Product Code:Product 14","iMac"]:
            assert True
        else:
            assert False

