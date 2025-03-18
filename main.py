from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
import msvcrt
import warnings
import unittest

STEP_BY_STEP = False


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        # Selenium uyarılarını devre dışı bırak
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        
        # Chrome options ayarları
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')  # Sadece fatal hataları göster
        chrome_options.add_experimental_option('detach', True)
        
        # WebDriver'ı options ile başlat
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def test_add_to_cart(self):
        # 1.  Go to https://www.amazon.com.tr/ s
        home_page = HomePage(self.driver)
        home_page.go_to_url("https://www.amazon.com.tr/")
        home_page.accept_cookies()
        print("Amazon.com.tr ana sayfasına gidildi ve çerezler kabul edildi.")

        print("Devam etmek için bir tuşa basın... ( 1. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 2.  Verify that you are on the home page 
        if home_page.is_on_homepage(): print("Anasayfaya ulaşıldığı doğrulandı.")
        self.assertTrue(home_page.is_on_homepage(),"This is not homepage!")

        print("Devam etmek için bir tuşa basın... ( 2. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 3.  Type 'search term' in the search field at the top of the screen and perform search.
        search_term = "samsung"
        home_page.search_field(search_term)
        print(f"'{search_term}' aramasının yapılması için komut verildi.")

        print("Devam etmek için bir tuşa basın... ( 3. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 4.  Verify that there are results for search term on the page that appears. 
        if home_page.is_on_searchpage(search_term): print(f"{search_term} arama sonuçları sayfasına ulaşıldığı doğrulandı.")
        self.assertTrue(home_page.is_on_searchpage(search_term),f"This is not {search_term} search page!")
 
        print("Devam etmek için bir tuşa basın... ( 4. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 5.  Click on the 2nd page from the search results and verify that the 2nd page is currently displayed on the page that opens. 
        page_number = 2
        home_page.go_to_page_number(page_number)
        if home_page.is_on_searchpage(search_term, page_number): print(f"{page_number}. sayfaya gitme komutu verildi ve sayfaya ulaşıldığı doğrulandı.")
        self.assertTrue(home_page.is_on_searchpage(search_term, page_number),f"This is not {search_term} and {page_number}. search page!")

        print("Devam etmek için bir tuşa basın... ( 5. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 6.  Go to the 3rd Product page from the top 
        item_number = 3
        category_page = CategoryPage(self.driver)
        category_page.click_visible_product(item_number)
        print( f"{item_number}. ürüne tıklama komutu verildi.")

        print("Devam etmek için bir tuşa basın... ( 6. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 7.  Verify that you are on the product page 
        product_page = ProductPage(self.driver)
        if product_page.is_on_product_page(): print("Ürün sayfasına ulaşıldı.")
        self.assertTrue(product_page.is_on_product_page(),f"This is not a product page!")

        print("Devam etmek için bir tuşa basın... ( 7. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 8.  Add the product to the cart 
        product_name = category_page.add_to_cart_product()
        if product_name: print(f"{product_name} ürünü sepete eklendi ve kontrol için kaydedildi.")
        # Ürünün başlığını kaydet

        print("Devam etmek için bir tuşa basın... ( 8. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 9.  Verify that the product has been added to the cart
        if product_page.is_on_cart_added_page(): print("Ürün sepete ekleme sayfasına ulaşıldı.")

        print("Devam etmek için bir tuşa basın... ( 9. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 10. Go to the cart page
        if home_page.go_to_url("https://www.amazon.com.tr/cart"): print("Sepet sayfasına gitme komutu verildi.")

        print("Devam etmek için bir tuşa basın... ( 10. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 11. Verify that you are on the cart page and that the correct product has been added to the cart 
        if product_page.is_on_cart_page(): print("Sepet sayfasına ulaşıldı.")
        if product_page.cart_verify(product_name): print("Ürün sepete eklenmiş ve doğru ürün sepete eklenmiş.")

        print("Devam etmek için bir tuşa basın... ( 11. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()

        # 12. Delete the product from the cart and verify that it has been deleted 

        if product_page.cart_delete(product_name): print("Ürünü sepetten silme komutu verildi.")
        if not product_page.cart_verify(product_name): print("Ürünün sepetten silindiği doğrulandı.")

        print("Devam etmek için bir tuşa basın... ( 12. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()


        # 13. Return to the home page and verify that it is on the home page
        home_page = HomePage(self.driver)
        home_page.go_to_url("https://www.amazon.com.tr/")
        print("Amazon.com.tr ana sayfasına gidildi.")
        if home_page.is_on_homepage(): print("Anasayfaya ulaşıldığı doğrulandı.")
        self.assertTrue(home_page.is_on_homepage(),"This is not homepage!")

        print("Devam etmek için bir tuşa basın... ( 13. ADIM İŞLENDİ! )")
        if STEP_BY_STEP: msvcrt.getch()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()