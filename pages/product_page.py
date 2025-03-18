from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import html


class ProductPage(BasePage):

    # Product page locators
    PRODUCT_TITLE = (By.ID, "productTitle")
    PRODUCT_IMAGE_GRID = (By.CSS_SELECTOR, "div.a-fixed-left-grid")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_ITEMS = (By.CSS_SELECTOR, "span.a-truncate-cut")


    def __init__(self, driver):
        super().__init__(driver)

    def is_on_product_page(self, timeout=10):
        locator = (By.CSS_SELECTOR, f"#{self.PRODUCT_TITLE[1]}, #{self.ADD_TO_CART_BUTTON[1]}, {self.PRODUCT_IMAGE_GRID[1]}")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_on_cart_added_page(self):
        expected_url = "https://www.amazon.com.tr/cart/smart-wagon?newItems="
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)
    
    def is_on_cart_page(self):
        expected_url = "https://www.amazon.com.tr/cart"
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)
    
    def cart_verify(self, product_name):
        try:
            # Wait for cart items to be visible
            cart_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
            
            # Get all item names and clean them
            for item in cart_items:
                item_text = item.text.strip()
                # Remove ellipsis if present
                if item_text.endswith('...'):
                    item_text = item_text[:-3].strip()

                if item_text.lower() in product_name.lower() or product_name.lower() in item_text.lower():
                    return True
                    
            return False
            
        except TimeoutException:
            return False
        
    def cart_delete(self, product_name):
        try:
            # Sepet öğelerinin görünür olmasını bekle
            cart_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
            
            # Tüm sepet öğelerinin adlarını al
            for item in cart_items:
                item_text = item.text.strip()
                # Üç nokta varsa kaldır
                if item_text.endswith('...'):
                    item_text = item_text[:-3].strip()
                    
                # Ürün adı eşleşiyor mu kontrol et
                if item_text.lower() in product_name.lower() or product_name.lower() in item_text.lower():
                    
                    # Bu öğenin bulunduğu satırı tespit et
                    # Ana konteyner seviyesine kadar git
                    parent = item
                    for _ in range(10):  # Maksimum 10 seviye yukarı çık
                        try:
                            # HTML class adını kontrol et
                            if "sc-list-item-content" in parent.get_attribute("class") or "sc-action-links" in parent.get_attribute("class"):
                                break
                            
                            # Bir üst seviyeye git
                            parent = parent.find_element(By.XPATH, "./..")
                        except:
                            break
                    
                    # Bu konteyner içindeki silme düğmesini bul

                    # Özel CSS seçicisiyle silme butonunu bul
                    delete_button = parent.find_element(By.CSS_SELECTOR, "input[data-action='delete']")
                    
                    if delete_button:
                        # JavaScript ile tıklama yap (daha güvenilir)
                        self.driver.execute_script("arguments[0].click();", delete_button)
                        
                        # Silme işleminin tamamlanmasını bekle
                        import time
                        time.sleep(2)
                        return True
            return False
            
        except Exception as e:
            return False