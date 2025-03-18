from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    # Product page locators
    PRODUCT_TITLE = (By.ID, "productTitle")
    PRODUCT_IMAGE_GRID = (By.CSS_SELECTOR, "div.a-fixed-left-grid")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")


    def __init__(self, driver):
        super().__init__(driver)

    def is_on_product_page(self, timeout=10):
        try:
            self.WebDriverWait(self.driver, timeout).until(
                self.EC.presence_of_all_elements_located([
                    self.PRODUCT_TITLE,
                    self.ADD_TO_CART_BUTTON,
                    self.PRODUCT_IMAGE_GRID
                ])
            )
            return True
        except self.TimeoutException:
            return False

    def is_on_cart_added_page(self):
        expected_url = "https://www.amazon.com.tr/cart/smart-wagon?newItems="
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)
    
    def is_on_cart_page(self):
        expected_url = "https://www.amazon.com.tr/cart"
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)