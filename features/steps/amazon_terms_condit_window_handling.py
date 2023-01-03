from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.XPATH, "//p // a[@href='https://www.amazon.com/privacy']")
PRIVACY_TEXT = (By.XPATH, "//div[@class = 'cs-help-content'] // h1")


@given("Open Amazon T&C page")
def amazon_tc(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html"
                       "/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store all the original windows")
def stored_amazon_terms_cond_windows(context):
    context.original_tc_windows = context.driver.current_window_handle
    print(context.original_tc_windows)
    old_window = context.driver.current_window_handle
    print(old_window)


@when("Click on Amazon Privacy Notice link")
def privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when("Switch to the newly opened t&c window")
def switch_privacy_link(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.old_windows = context.driver.window_handles
    print(context.old_windows)
    context.driver.switch_to.window(context.old_windows[1])


@then("verify Amazon Privacy Notice page is opened")
def is_privacy_opened(context):
    context.driver.wait.until(EC.text_to_be_present_in_element(PRIVACY_TEXT, "Privacy Notice"))


@then("User can close new window and switch back to original")
def go_back_to_tc(context):
    context.driver.close()
    context.driver.switch_to.window(context.old_windows[0])
    # or context.driver.switch_to.window(context.original_tc_windows)


@then("Verify Amazon T&C page is reopened")
def is_it_original_tc(context):
    context.driver.wait.until(EC.url_contains('notification_condition_of_use'))
