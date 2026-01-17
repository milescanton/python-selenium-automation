from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_PAGE_TEXT = (By.XPATH, "//h1[contains(@class,'styles_ndsHeading__phw6r')]")

    def verify_sign_in_page(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN_PAGE_TEXT)