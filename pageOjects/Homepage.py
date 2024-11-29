import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


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
        z = self.driver.title
        print(y,z)
        return y,z

    def components(self):
        actions = ActionChains(self.driver)
        self.driver.refresh()
        web_element = self.driver.find_element(By.LINK_TEXT,"Components")
        actions.move_to_element(web_element).perform()
        time.sleep(2)
        # self.driver.find_element(By.LINK_TEXT,"Monitors (2)").click()

        elements = self.driver.find_elements(By.XPATH,"//a")
        for i in elements:
                if i.text == "Monitors (2)":
                    i.click()
                    break

        x =self.driver.find_element(By.XPATH,"(//button[@type='button'])[9]")
        x.click()
        time.sleep(5)
        self.driver.find_element(By.NAME,"option[218]").click()
        time.sleep(3)
        y = self.driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
        for i in y:
            i.click()
        self.driver.find_element(By.NAME,"option[208]").send_keys("test1234")
        Select(self.driver.find_element(By.ID,"input-option217")).select_by_value("3")
        self.driver.find_element(By.ID,"input-option209").send_keys("summary")
        path = "C:/Users/2148389/OneDrive - Cognizant/Documents/bitbucket certificate.pdf"
        time.sleep(5)
        self.driver.find_element(By.ID,"button-upload222").send_keys(path)
        time.sleep(2)
        self.driver.find_element(By.NAME,"option[219]").clear()
        self.driver.find_element(By.NAME, "option[219]").send_keys("2011-02-20")
        self.driver.find_element(By.NAME,"option[221]").clear()
        self.driver.find_element(By.NAME,"option[221]").send_keys("22:25")
        self.driver.find_element(By.NAME,"option[220]").clear()
        self.driver.find_element(By.NAME, "option[220]").send_keys("2011-02-20 22:25")
        self.driver.find_element(By.NAME,"quantity").clear()
        self.driver.find_element(By.NAME, "quantity").send_keys("2")
        time.sleep(4)
        self.driver.find_element(By.ID,"button-cart").click()
        time.sleep(4)
        # print(self.driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text())
        # return self.driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text()










