import time

from pageOjects.ProductsDisplay import Display
from pageOjects.Search import Search
from utilities.readProperties import ReadConfig


class TestDisplay():
    baseURL = ReadConfig.getApplicationURL()

    def test_product_display(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.dp = Display(self.driver)
        self.dp.search_existing("iMac")
        self.dp.search_button()
        self.dp.img_link()
        self.dp.major_thumbnail()
        self.dp.escape_thumbnail()
        if self.dp.escape_button() == "iMac":
            assert True
        else:
            assert False

        self.dp.minor_thumbnail()
        time.sleep(5)
        if self.dp.escape_button() =="iMac":
            assert True
        else:
            assert False
        time.sleep(5)
        self.dp.second_minor()
        if self.dp.escape_button() == "iMac":
            assert True
        else:
            assert False
