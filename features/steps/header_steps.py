from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TARGET_CIRCLE = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


# @when('Click Target Circle')
# def click_target_circle(context):
#     context.driver.find_element(*TARGET_CIRCLE).click()
#
#
# @when('Click Account button')
# def click_account_button(context):
#     context.driver.find_element(By.ID, 'account-sign-in').click()
#
#
# @then('Click Sign In button')
# def click_sign_in_button(context):
#     context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()