from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    def verify_empty_cart_msg(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
        assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"