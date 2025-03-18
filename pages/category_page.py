from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):
    CATEGORY_PAGE_PRODUCT_VIEW_ITEM = (By.XPATH,"(//*[@class='nav nav-pills nav-justified']//a)[{}]")
    CATEGORY_ITEMS = (By.XPATH,"(//*[@class='productinfo text-center'])[{}]")
    CATEGORY_ADD_TO_CART_BTN = (By.XPATH,"(//*[@class='productinfo text-center'])[{}]//a")


    def __init__(self, driver):
        super().__init__(driver)

    def go_to_product_item(self, index):
        self.click(self.CATEGORY_PAGE_PRODUCT_VIEW_ITEM[0],self.CATEGORY_PAGE_PRODUCT_VIEW_ITEM[1].format(index))

    def move_to_product(self,index):
        self.move_to_element(self.CATEGORY_ITEMS[0],self.CATEGORY_ITEMS[1].format(index))

    def add_to_cart_product(self,index):
        self.click(self.CATEGORY_ADD_TO_CART_BTN[0],self.CATEGORY_ADD_TO_CART_BTN[1].format(index))