from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_on_searchpage(self, search_term):
        expected_title = f"Amazon.com.tr : {search_term}"
        return  expected_title.__eq__(self.get_title())