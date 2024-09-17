from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Home:
    #locators
    txt_account = "//i[@class='fa fa-user']"
    txt_register = "//a[normalize-space()='Register']"
    txt_login = "//a[normalize-space()='Login']"
    txt_logout = "(//a[normalize-space()='Logout'])[1]"
    text_desk = "//a[text()='Desktops']"
    txt_show = "//a[text()='Show AllDesktops']"
    compare_link = "//a[@id='compare-total']"
    not_chosen ="//p[text()='You have not chosen any products to compare.']"
    btn_continue = "//a[text()='Continue']"
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

    def hover_desk(self):
        actions = ActionChains(self.driver)
        element1 = self.driver.find_element(By.XPATH,self.text_desk)
        element2 = self.driver.find_element(By.XPATH,self.txt_show)
        actions.move_to_element(element1).perform()
        actions.move_to_element(element2).click().perform()
        self.driver.find_element(By.XPATH,self.compare_link).click()
        return self.driver.title

    def chosen_desk(self):
        actions = ActionChains(self.driver)
        element1 = self.driver.find_element(By.XPATH,self.text_desk)
        element2 = self.driver.find_element(By.XPATH,self.txt_show)
        actions.move_to_element(element1).perform()
        actions.move_to_element(element2).click().perform()
        self.driver.find_element(By.XPATH,self.compare_link).click()
        y = self.driver.find_element(By.XPATH,self.not_chosen).text
        self.driver.find_element(By.XPATH,self.btn_continue).click()
        return y,self.driver.title







