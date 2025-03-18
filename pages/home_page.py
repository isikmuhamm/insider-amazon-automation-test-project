from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_on_homepage(self):
        expected_title = "Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev, mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi"
        return  expected_title.__eq__(self.get_title())
    
    def is_on_searchpage(self, search_term, page_number = 1):
        if page_number > 1:
            expected_url = f"https://www.amazon.com.tr/s?k={search_term}&page={page_number}"
        else:
            expected_url = f"https://www.amazon.com.tr/s?k={search_term}"
        return self.get_url().startswith(expected_url)