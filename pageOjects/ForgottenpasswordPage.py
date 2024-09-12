from selenium.webdriver.common.by import By


class EnterMail():
    # locators
    user_email = "//input[@id='input-email']"
    user_password = "//input[@id='input-password']"
    button = "//input[@value='Login']"
    forgotten_link = "//div[@class='form-group']//a[contains(text(),'Forgotten Password')]"
    enter_email = "//input[@id='input-email']"
    button_continue = "//input[@value='Continue']"
    reset_link = "//div[@class='alert alert-success alert-dismissible']"
    def __init__(self, driver):
        self.driver = driver

    def login_email(self, email):
        Email_enter = self.driver.find_element(By.XPATH, self.user_email)
        Email_enter.send_keys(email)

    def login_password(self, password):
        txt_pass = self.driver.find_element(By.XPATH, self.user_password)
        txt_pass.send_keys(password)

    def click(self):
        self.driver.find_element(By.XPATH, self.button).click()

    def forgot_email_enter(self, mail):
        self.driver.find_element(By.XPATH, self.enter_email).send_keys(mail)

    def click_continue(self):
        return self.driver.find_element(By.XPATH,self.button_continue).click()
    def link_sent(self):
       return  self.driver.find_element(By.XPATH,self.reset_link).text