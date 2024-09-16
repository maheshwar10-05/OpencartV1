from pageOjects.Search import Search
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig


class Test_Site():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_site_map(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.site_map()
        if self.srch.site_map() == "Search":
            assert True
        else:
            assert False


