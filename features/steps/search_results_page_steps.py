from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'

@then('Click Add to Cart Button')
def click_add_to_cart_button(context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR, 'button#addToCartButtonOrTextIdFor54212642').click()

@then('Click 2nd Add to Cart Button')
def click_2nd_add_to_cart_button(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Add to cart for Brownberry Healthy Multi Grain Bread - 24oz']").click()

@then('Click View Cart Button')
def click_view_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()


