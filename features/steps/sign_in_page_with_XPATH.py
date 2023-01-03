from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

AMAZON_HOME_PAGE = ('https://www.amazon.com')
SIGN_IN_BTN = (By.XPATH, "//div[@id='nav-tools']//a[contains(@href, "
                         "'ct&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth')]")
EMAIL_FIELD = (By.XPATH, "//div[@class='a-row a-spacing-base']/input[@type='email']")
ERROR_TEXT = (By.XPATH, "//div[@class='a-section']//h4")
T_C = (By.XPATH, "//div[@id='legalTextRow']/a[contains(@href,'ie=UTF8&nodeId=508088')]")
T_C_TEXT = (By.XPATH, "//div[@class='help-content'] / h1")


@given("Open Amazon Page")
def amazon_home_page(context):
    context.driver.get(AMAZON_HOME_PAGE)


@when('Select: Hello, Sign In Account and Lists')
def select_sign_in_btn(context):
    sleep(3)
    sign_in = context.driver.find_element(*SIGN_IN_BTN).click()


@then('Verify user on the {word} page')
def is_sign_in(context, word):
    actual_current_url = context.driver.current_url
    assert word in actual_current_url, f"Expected word {word} not in actual url:\n" \
                                       f"{actual_current_url}"


@then("Fill up email/phone field: {given_credential}")
def given_email_credential(context, given_credential):
    email_field = context.driver.find_element(*EMAIL_FIELD)
    email_field.clear()
    email_field.send_keys(given_credential, Keys.ENTER)


@then("Verify Error Message: {error_text}")
def is_error(context, error_text):
    actual_text = context.driver.find_element(*ERROR_TEXT).text
    assert error_text == actual_text, f"Expected text was {error_text}, but user got {actual_text}"

@when("Select Conditions of Use")
def terms_conditions(context):
    context.driver.find_element(*T_C).click()

@then("Verify {t_c} is the page")
def is_tc(context,t_c):
    actual_text = context.driver.find_element(*T_C_TEXT).text
    assert t_c == actual_text, f"Expected text is {t_c}, but the user got {actual_text}"

@then("Go Back and Refresh the Page")
def lets_go_back(context):
    context.driver.back()
    context.driver.refresh()

