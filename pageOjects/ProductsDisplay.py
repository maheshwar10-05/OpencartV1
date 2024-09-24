import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Display():
    txt_search_bar = "//input[@placeholder='Search']"
    src_txt = "input[name='search']"
    clk_search = "//button[@class='btn btn-default btn-lg']"
    img = "//img[@title='iMac']"
    thumbnail = "//ul[@class='thumbnails']//li[1]//a[1]"
    right_arrow = "//button[@title='Next (Right arrow key)']"
    left_arrow = "//button[@title='Previous (Left arrow key)']"
    esc_button = "//button[text()='×']"
    smallthumbnail = "//li[2]//a[1]//img[1]"
    second_small = "(//img[@title='iMac'])[3]"
    prod_text = "//h1[text()='iMac']"

    def __init__(self, driver):
        self.driver = driver

    def search_existing(self, product):
        product_text = self.driver.find_element(By.XPATH, self.txt_search_bar)
        product_text.send_keys(product)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.clk_search).click()

    def img_link(self):
        self.driver.find_element(By.XPATH, self.img).click()

    def major_thumbnail(self):
        self.driver.find_element(By.XPATH, self.thumbnail).click()

    def escape_thumbnail(self):
        for i in range(1, 3):
            self.driver.find_element(By.XPATH, self.right_arrow).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.left_arrow).click()

    def escape_button(self):
        self.driver.find_element(By.XPATH, self.esc_button).click()
        time.sleep(4)
        x = self.driver.title
        return x

    def minor_thumbnail(self):
        self.driver.find_element(By.XPATH, self.smallthumbnail).click()
        for i in range(1, 3):
            self.driver.find_element(By.XPATH, self.right_arrow).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.left_arrow).click()

    def second_minor(self):
        self.driver.find_element(By.XPATH, self.second_small).click()
        for i in range(1, 3):
            self.driver.find_element(By.XPATH, self.right_arrow).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.left_arrow).click()

    def list_product_name(self):
        var = self.driver.find_element(By.XPATH,self.prod_text).text
        empty_list = []
        for i in range(1, 3):
            x = self.driver.find_elements(By.XPATH, "//div[@class='col-sm-4']//ul[1]//li[" + str(i) + "]")

            for i in x:
                empty_list.append(i.text)
        empty_list.append(var)
        print(empty_list)
        return empty_list


