from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In page')
def verify_sign_in_page(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles_ndsHeading__phw6r')]").text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    print(actual_text)
