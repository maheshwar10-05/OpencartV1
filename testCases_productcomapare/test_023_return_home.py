from pageOjects.Homepage import Home
from utilities.readProperties import ReadConfig


class Test_return():
    baseURL = ReadConfig.getApplicationURL()

    def test_homepage_displayed(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        if self.hp.chosen_desk() == ("You have not chosen any products to compare.", "Your Store"):
            assert True

        else:
            assert False
