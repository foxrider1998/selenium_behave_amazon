from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BAR = (By.CSS_SELECTOR, "div.nav-fill #twotabsearchtextbox")
SEARCH_ICON = (By.CSS_SELECTOR, 'div.nav-right input[type="submit"]')
SEARCH_DESCRIPTION = (By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']"
                                "//span[contains(@class, 'a-text-bold')]")
SEARCH_COUNT = (By.CSS_SELECTOR, "div.sg-col-inner div.sg-col-inner")


@given("Navigate to {website}")
def go_to_this_page(context, website):
    context.driver.get(website)


@when("Locate The Search Bar")
def is_search_bar(context):
    context.driver.find_element(*SEARCH_BAR)


@when("Search for {search_item} and click Search Icon")
def is_search_icon(context, search_item):
    send_it = context.driver.find_element(*SEARCH_BAR)
    send_it.clear()
    send_it.send_keys(search_item)
    context.driver.find_element(*SEARCH_ICON).click()


@then("Verify {search_item} is in url")
def is_search_in_url(context, search_item):
    actual_url = context.driver.current_url
    assert search_item in actual_url, f"{search_item} is missing from current url"


@then("Verify {search_result} is in Page Description")
def is_search_in_description(context, search_result):
    actual = context.driver.find_element(*SEARCH_DESCRIPTION).text
    assert search_result == actual.lower(), f"Expected result was {search_result}, but got {actual} instead"


@then("Verify at least {num} of items in the page search result")
def is_count(context, num):
    total_count = context.driver.find_elements(*SEARCH_COUNT)
    print(len(total_count))
    assert int(num) <= len(total_count), f"at least {num} of items were expected, actual count was {len(total_count)}"
