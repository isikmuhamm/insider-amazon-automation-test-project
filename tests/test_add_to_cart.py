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
        # 1.  Go to https://www.amazon.com.tr/ 
        home_page = HomePage(self.driver)
        home_page.go_to_url("https://www.amazon.com.tr/")

        # 2.  Verify that you are on the home page 
        self.assertTrue(home_page.is_on_homepage(),"This is not homepage!")

        # 3.  Type 'search term' in the search field at the top of the screen and perform search.
        search_term = "samsung"
        home_page.search_field(search_term)

        # 4.  Verify that there are results for search term on the page that appears. 
        self.assertTrue(home_page.is_on_searchpage(search_term),f"This is not {search_term} search page!")
 
        # 5.  Click on the 2nd page from the search results and verify that the 2nd page is currently displayed on the page that opens. 
        page_number = 2
        home_page.go_to_page_number(page_number)
        self.assertTrue(home_page.is_on_searchpage(search_term, page_number),f"This is not {search_term} and {page_number}. search page!")

        # 6.  Go to the 3rd Product page from the top 
        item_number = 3
        category_page = CategoryPage(self.driver)
        category_page.click_visible_product(item_number)

        # 7.  Verify that you are on the product page 
        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.is_on_product_page(),f"This is not a product page!")

        # 8.  Add the product to the cart 
        product_name = category_page.add_to_cart_product()
        # Ürünün başlığını kaydet

        # 9.  Verify that the product has been added to the cart
        product_page.is_on_cart_added_page()

        # 10. Go to the cart page
        home_page.go_to_url("https://www.amazon.com.tr/cart")

        # 11. Verify that you are on the cart page and that the correct product has been added to the cart 
        product_page.is_on_cart_page


        category_page.move_to_product(2)
        sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
"""
11. Verify that you are on the cart page and that the correct product has been added to 
the cart 
12. Delete the product from the cart and verify that it has been deleted 
13. Return to the home page and verify that it is on the home page
"""