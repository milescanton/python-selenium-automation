from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"


@then('Verify Cart')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('\nProduct in cart:')
    print(product_in_cart)
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]} but got {product_in_cart[:20]}'