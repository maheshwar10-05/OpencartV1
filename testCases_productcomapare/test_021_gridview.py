import pytest

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageOjects.Search import Search


class Test_grid():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.run(order = 3)
    def test_grid_view(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_existing("iMac")
        self.srch.search_button()
        self.validate = self.srch.grid_view()
        if self.validate == ("Success: You have added iMac to your product comparison! ×", "Compare this Product"):
            assert True
        self.link = self.srch.product_link_detail()
        if self.link == "Product Details":
            assert True
        else:
            assert False
