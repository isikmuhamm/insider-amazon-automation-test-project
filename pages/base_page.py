from lib2to3.pgen2.driver import Driver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    NAVBAR_ELEMENTS = (By.XPATH, "//*[@class='shop-menu pull-right']//a[text()='{}']")
    AMAZON_SEARCH_BAR = (By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.action = ActionChains(driver)

    def go_to_url(self,url):
        self.driver.get(url)

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
