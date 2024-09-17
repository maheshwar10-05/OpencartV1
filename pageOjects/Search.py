import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


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
    img = "//img[@title='iMac']"
    com_prod = "//button[@type='button' and contains(@data-original-title,'Compare this Product')]"
    success_text = "//div[@class='alert alert-success alert-dismissible']"
    prouct_link = "//a[text()='product comparison']"
    product_details = "//td[@colspan='2']//strong[text()='Product Details']"
    listview = "//button[@id='list-view']"
    gridview = "//button[@id='grid-view']"

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
        x = self.driver.title, self.driver.current_url, self.driver.find_element(By.XPATH, self.search_title).text
        empty.append(x)
        print(empty)
        return empty

    def img_link(self):
        self.driver.find_element(By.XPATH, self.img).click()

    def hover_move(self):
        element_hover = self.driver.find_element(By.XPATH, self.com_prod)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_hover).perform()
        tooltip_text = element_hover.get_attribute("data-original-title")
        self.driver.save_screenshot(
            "C:/Users/2148389/PycharmProjects/OpenCartV1" + "\\screenshots\\" + "productcomapare2.png")
        actions.move_to_element(element_hover).click().perform()
        time.sleep(4)
        y = self.driver.find_element(By.XPATH, self.success_text).text
        print(tooltip_text, y)
        return tooltip_text, y

    def product_link_detail(self):
        self.driver.find_element(By.XPATH, self.prouct_link).click()
        x = self.driver.find_element(By.XPATH, self.product_details).text
        print(x)
        return x

    def list_view(self):
        self.driver.find_element(By.XPATH, self.listview).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element_hover = self.driver.find_element(By.XPATH, self.com_prod)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_hover).perform()
        tooltip_text = element_hover.get_attribute("data-original-title")
        actions.move_to_element(element_hover).click().perform()
        time.sleep(4)
        y = self.driver.find_element(By.XPATH, self.success_text).text
        print(tooltip_text,y)
        return tooltip_text,y

    def grid_view(self):
        self.driver.find_element(By.XPATH, self.gridview).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element_hover = self.driver.find_element(By.XPATH, self.com_prod)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_hover).perform()
        tooltip_text = element_hover.get_attribute("data-original-title")
        actions.move_to_element(self.driver.find_element(By.XPATH, self.com_prod)).click().perform()
        time.sleep(4)
        y = self.driver.find_element(By.XPATH, self.success_text).text
        print(tooltip_text,y)
        return tooltip_text, y
