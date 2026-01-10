from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")  # always clicks on 1st Add to cart btn
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'


@then('Click Add to Cart Button')
def click_add_to_cart_button(context):
    sleep(10)
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn


@then('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print("Name saved: ")
    # print(context.product_before_adding)


@then('Click 2nd Add to Cart Button')
def click_2nd_add_to_cart_button(context):
    context.driver.wait.until(
        EC.presence_of_element_located(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side Navigation Add to Cart button did not appear'
    )
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@then('Click View Cart Button')
def click_view_cart_button(context):
    context.driver.wait.until(
        EC.presence_of_element_located(SIDE_NAV_VIEW_CART_BTN),
        message='Side Navigation View Cart button did not appear'
    )
    context.driver.find_element(*SIDE_NAV_VIEW_CART_BTN).click()




