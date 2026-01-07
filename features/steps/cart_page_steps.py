from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"

@then('Verify Cart')
def verify_cart(context):
    item_name = context.driver.find_element(By.XPATH, "//div[text()='Brownberry Healthy Multi Grain Bread - 24oz']").text
    print(item_name)