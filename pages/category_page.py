from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):
    CATEGORY_PAGE_PRODUCT_VIEW_ITEM = (By.XPATH,"(//*[@class='nav nav-pills nav-justified']//a)[{}]")
    CATEGORY_ITEMS = (By.XPATH,"(//*[@class='productinfo text-center'])[{}]")
    CATEGORY_ADD_TO_CART_BTN = (By.XPATH,"//*[@id='add-to-cart-button']")
    VISIBLE_PRODUCT_LINK = (By.XPATH, "(//*[@data-component-type='s-search-result'][not(@style='display: none')]//a[contains(@class,'a-link-normal') and contains(@class,'s-line-clamp-4')])[{}]")
    PRODUCT_TITLE = (By.ID, "productTitle")



    def __init__(self, driver):
        super().__init__(driver)

    def go_to_product_item(self, index):
        self.click(self.CATEGORY_PAGE_PRODUCT_VIEW_ITEM[0],self.CATEGORY_PAGE_PRODUCT_VIEW_ITEM[1].format(index))

    def move_to_product(self,index):
        self.move_to_element(self.CATEGORY_ITEMS[0],self.CATEGORY_ITEMS[1].format(index))

    def add_to_cart_product(self):
        self.click(self.CATEGORY_ADD_TO_CART_BTN[0], self.CATEGORY_ADD_TO_CART_BTN[1])
        return self.PRODUCT_TITLE

    def click_visible_product(self, index):
        self.click(self.VISIBLE_PRODUCT_LINK[0], self.VISIBLE_PRODUCT_LINK[1].format(index))