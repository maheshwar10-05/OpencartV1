from selenium.webdriver.common.by import By

class MyAccountPage():
    txt_myaccount = "//a[@title='My Account']"
    txt_logout = "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver



    def click_myaccount(self):
        self.driver.find_element(By.XPATH,self.txt_myaccount).click()



    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.txt_logout).click()