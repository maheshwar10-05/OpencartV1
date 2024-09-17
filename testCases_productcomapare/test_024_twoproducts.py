import time

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageOjects.Search import Search


class Test_twoCompare():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_two_compare(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        time.sleep(5)
        self.srch.two_prod_display()
        time.sleep(5)
        self.srch.search_existing("iPhone")
        self.srch.search_button()
        self.srch.two_prod_display()
        time.sleep(5)
        self.srch.product_link_detail()
        if self.srch.table() == ["Product", "iMac", "iPhone"]:
            assert True
        else:
            assert False
