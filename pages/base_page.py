from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:

    NAVBAR_ELEMENTS = (By.XPATH, "//*[@class='shop-menu pull-right']//a[text()='{}']")
    AMAZON_SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    PAGE_NUMBER = (By.XPATH, "//a[@class='s-pagination-item s-pagination-button s-pagination-button-accessibility' and text()='{}']")
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "#sp-cc-accept")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.action = ActionChains(driver)

    def accept_cookies(self):
        try:
            cookie_button = self.wait_for_clickable(*self.ACCEPT_COOKIES_BUTTON)
            cookie_button.click()
        except TimeoutException:
            # Çerez bildirimi zaten kapanmış olabilir
            pass

    def go_to_url(self,url):
        self.driver.get(url)
        return True

    def get_title(self):
        return self.driver.title

    def wait_for_clickable(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by,locator)))

    def click(self, by, locator):
        self.wait_for_clickable(by,locator).click()

    def move_to_element(self, by, locator):
        element = self.wait_for_clickable(by,locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_element(self, by, locator):
        element = self.wait_for_clickable(by, locator)
        ActionChains(self.driver).scroll_to_element(element).perform()

    def search_field(self, search_term):
        search_box = self.wait_for_clickable(*self.AMAZON_SEARCH_BAR)
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.submit()
        self.wait_for_clickable(*self.AMAZON_SEARCH_BAR)
        return True

    def go_to_page_number(self, page_number):
        page_locator = (self.PAGE_NUMBER[0], self.PAGE_NUMBER[1].format(page_number))
        self.click(*page_locator)

    def click_visible_product(self, product_order):
        # Find all visible product links
        visible_products = self.driver.find_elements(By.CSS_SELECTOR, 
            "div[data-component-type='s-search-result']:not([style*='display: none']) a.a-link-normal.s-line-clamp-4")
        
        if not visible_products:
            raise Exception("No visible products found")
            
        if product_order < 1 or product_order > len(visible_products):
            raise Exception(f"Product order {product_order} is out of range. Available products: {len(visible_products)}")
        
        visible_products[product_order - 1].click()