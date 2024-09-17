from pageOjects.Homepage import Home
from utilities.readProperties import ReadConfig


class Test_Desktop():
    baseURL = ReadConfig.getApplicationURL()

    def test_product_comparison(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.hp.hover_desk()
        if self.hp.hover_desk() == "Product Comparison":
            assert True
        else:
            assert False
