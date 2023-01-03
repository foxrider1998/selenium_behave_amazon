from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

IMAGE_OF_DOG = (By.XPATH, '//img[@id="d"]')


@given("{bad} Page of Amazon")
def is_bad_page(context, bad):
    context.driver.get(bad)
    sleep(3)


@when("Store original windows")
def lets_store(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    sleep(3)


@then("Click to open blog")
def go_to_image(context):
    context.driver.find_element(*IMAGE_OF_DOG).click()
    sleep(3)


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.my_windows = context.driver.window_handles
    context.driver.switch_to.window(context.my_windows[1])
    sleep(3)


@when("User closes new window and goes back to old window")
def close_new_go_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)