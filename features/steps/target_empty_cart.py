from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


sleep(3)


@then('"Your cart is empty" message displays')
def verify_empty_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

