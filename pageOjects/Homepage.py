from selenium import webdriver
from selenium.webdriver.common.by import By


class Home:
    #locators
    txt_account = "//i[@class='fa fa-user']"
    txt_register = "//a[normalize-space()='Register']"
    txt_login = "//a[normalize-space()='Login']"
    txt_logout = "(//a[normalize-space()='Logout'])[1]"
    txt_search_bar = "//input[@placeholder='Search']"
    clk_search = "//button[@class='btn btn-default btn-lg']"
    dis_product = "//a[normalize-space()='Samsung Galaxy Tab 10.1']"
    def __init__(self, driver):
        self.driver = driver

    def clickaccount(self):
        self.driver.find_element(By.XPATH, self.txt_account).click()

    def clickregister(self):
        self.driver.find_element(By.XPATH, self.txt_register).click()

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.txt_login).click()
    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.txt_logout).click()

    def search_existing(self,product):
        product_text = self.driver.find_element(By.XPATH,self.txt_search_bar)
        product_text.send_keys(product)

    def search_button(self):
        self.driver.find_element(By.XPATH,self.clk_search).click()

    def product_dis(self):
        return self.driver.find_element(By.XPATH,self.dis_product).text

