from selenium import webdriver
from selenium.webdriver.common.by import By


class Register:
    #locators
    first_name = "//input[@id='input-firstname']"
    last_name = "//input[@id='input-lastname']"
    email = "//input[@id='input-email']"
    tel_phone = "//input[@id='input-telephone']"
    password = "//input[@id='input-password']"
    conf_password = "//input[@id='input-confirm']"
    subscribe = "//label[normalize-space()='Yes']"
    policy = "//input[@name='agree']"
    con_button = "//input[@value='Continue']"
    message = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstname(self, fname):
        txt_fname = self.driver.find_element(By.XPATH, self.first_name)
        txt_fname.send_keys(fname)

    def setLastname(self, lname):
        txt_lname = self.driver.find_element(By.XPATH, self.last_name)
        txt_lname.send_keys(lname)

    def setEmail(self, email):
        txt_email = self.driver.find_element(By.XPATH, self.email)
        txt_email.send_keys(email)

    def setTelephone(self,num):
        num_value = self.driver.find_element(By.XPATH,self.tel_phone)
        num_value.send_keys(num)
    def setPassword(self, pwd):
        pasword_txt = self.driver.find_element(By.XPATH, self.password)
        pasword_txt.send_keys(pwd)

    def setConfirmPassword(self,confpwd):
        txt_confpass = self.driver.find_element(By.XPATH,self.conf_password)
        txt_confpass.send_keys(confpwd)

    def txtsub(self):
        self.driver.find_element(By.XPATH, self.subscribe).click()

    def txtpol(self):
        self.driver.find_element(By.XPATH, self.policy).click()

    def clickbutton(self):
        self.driver.find_element(By.XPATH, self.con_button).click()

    def conf(self):
        try:
            return self.driver.find_element(By.XPATH,self.message).text
        except:
            return None

