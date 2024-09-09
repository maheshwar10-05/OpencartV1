from selenium.webdriver.common.by import By


class LoginPage():
    # locators
    user_email = "//input[@id='input-email']"
    user_password = "//input[@id='input-password']"
    button = "//input[@value='Login']"
    message = "//h2[normalize-space()='My Account']"
    error_message = "//div[@class='alert alert-danger alert-dismissible']"
    out_message = "//h1[normalize-space()='Account Logout']"
    forgotten_link = "//div[@class='form-group']//a[contains(text(),'Forgotten Password')]"
    forg_message = "//h1[normalize-space()='Forgot Your Password?']"

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

    def confirmation(self):
        conf_message = self.driver.find_element(By.XPATH, self.message)
        return conf_message.text

    def invalid_confirmation(self):
        inv_message = self.driver.find_element(By.XPATH, self.error_message)
        return inv_message.text

    def login_out(self):
        conf_out = self.driver.find_element(By.XPATH, self.out_message)
        return conf_out.text
    def forgot_pass(self):
        self.driver.find_element(By.XPATH,self.forgotten_link).click()

    def conf_forgotten(self):
        return self.driver.find_element(By.XPATH,self.forg_message).text
