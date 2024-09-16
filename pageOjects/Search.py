from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Search:
    txt_search_bar = "//input[@placeholder='Search']"
    src_txt = "input[name='search']"
    clk_search = "//button[@class='btn btn-default btn-lg']"
    dis_product, dis_non = "//a[text()='iMac']", "//p[contains(text(),'There is no product that matches the search criter')]"
    products = "//div[@class='caption']//a[text()]"
    criteria_text = "//input[@id='input-search']"
    button_search = "//input[@id='button-search']"
    ck_box = "//input[@id='description']"
    ck_text = "//p[contains(text(),'Just when you thought iMac had everything, now the')]"
    drp_down = "//select[@name='category_id']"
    sub_ck_box = "//label[text()='Search in subcategories']"
    sitemap = "//a[text()='Site Map']"
    search_link = "//a[text()='Search']"
    search_title = "//h1[text()='Search']"

    def __init__(self, driver):
        self.driver = driver

    def search_existing(self, product):
        product_text = self.driver.find_element(By.XPATH, self.txt_search_bar)
        product_text.send_keys(product)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.clk_search).click()

    def product_dis(self):
        return self.driver.find_element(By.XPATH, self.dis_product).text

    def non_existing(self):
        return self.driver.find_element(By.XPATH, self.dis_non).text

    def search_products(self):
        empty = []
        k = self.driver.find_elements(By.XPATH, self.products)
        for i in k:
            empty.append(i.text)
        return empty

    def searching(self):
        product_text = self.driver.find_element(By.CSS_SELECTOR, self.src_txt)
        return product_text.get_attribute("placeholder")

    def criteria(self, txt):
        self.driver.find_element(By.XPATH, self.criteria_text).send_keys(txt)

    def btn_src(self):
        self.driver.find_element(By.XPATH, self.button_search).click()

    def check_box(self):
        self.driver.find_element(By.XPATH, self.ck_box).click()

    def desc_text(self):
        return self.driver.find_element(By.XPATH, self.ck_text).text

    def categories(self):
        choose = Select(self.driver.find_element(By.XPATH, self.drp_down))
        choose.select_by_value("27")

    def wrng_category(self):
        choose = Select(self.driver.find_element(By.XPATH, self.drp_down))
        choose.select_by_value("26")

    def sub_category(self):
        choose = Select(self.driver.find_element(By.XPATH, self.drp_down))
        choose.select_by_visible_text("Desktops")

    def sub_check_box(self):
        self.driver.find_element(By.XPATH, self.sub_ck_box).click()

    def site_map(self):
        self.driver.find_element(By.XPATH, self.sitemap).click()
        self.driver.find_element(By.XPATH, self.search_link).click()
        return self.driver.title

    def valid_page_verify(self):
        empty = []
        x = self.driver.title,self.driver.current_url,self.driver.find_element(By.XPATH,self.search_title).text
        empty.append(x)
        print(empty)
        return empty

