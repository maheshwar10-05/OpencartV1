import time

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageOjects.Search import Search


class Test_add():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_add_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        self.srch.add_shopping()
        time.sleep(5)
        self.srch.product_link_detail()
        time.sleep(5)
        self.srch.add_cart_product()
        if self.srch.sucess_shopping_message() == "Success: You have added iMac to your shopping cart! ×":
            assert True
        else:
            assert False
