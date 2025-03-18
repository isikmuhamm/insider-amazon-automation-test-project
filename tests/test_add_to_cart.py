from time import sleep

from selenium import webdriver
import unittest

from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_add_to_cart(self):
        # 1. Ana sayfaya git
        home_page = HomePage(self.driver)
        home_page.go_to_url("https://www.amazon.com.tr/")
        self.assertTrue(home_page.is_on_homepage(),"This is not homepage!")

        # 2. Arama terimiyle arama yap
        search_term = "samsung"
        home_page.search_field(search_term)
        self.assertTrue(home_page.is_on_searchpage(search_term),f"This is not {search_term} search page!")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # 3 producta git
        category_page = CategoryPage(self.driver)
        category_page.move_to_product(2)
        sleep(5)
        category_page.add_to_cart_product(1)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
