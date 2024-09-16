from pageOjects.Search import Search
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig


class Test_Validpage():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_page_valid(self, setup):
        self.logger.info("*** Test_001 started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.srch = Search(self.driver)
        self.srch.search_button()
        self.page = self.srch.valid_page_verify()
        if self.page == [('Search', 'https://tutorialsninja.com/demo/index.php?route=product/search', 'Search')]:
            assert True
        else:
            assert False
