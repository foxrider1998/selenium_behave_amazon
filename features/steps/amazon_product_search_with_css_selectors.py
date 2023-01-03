from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_HOME_PAGE = 'https://www.amazon.com'
SEARCH_BAR = (By.CSS_SELECTOR, "form#nav-search-bar-form input[type='text']")
SEARCH_ICON = (By.CSS_SELECTOR, "div.nav-right input[class*='rogressive-att']")
SEARCH_RESULT = (By.XPATH, "//div[@class='sg-col-inner']//span[contains(@class, 'tate a-text-bold')]")
ITEMS_IN_CART = (By.XPATH, "//div[@id='nav-cart-count-container']/ span[@id='nav-cart-count']")


@given('Go to Amazon Home Page')
def home_page_of_amazon(context):
    context.app.main_page.open_main_page()


@when("Navigate to the Search Bar and input {search_query}")
def search_for_item(context, search_query):
    context.app.main_page.input_amazon_search(search_query)  # Keys.ENTER)


@when("Click on Amazon Search Icon")
def click_on_search_icon(context):
    context.app.main_page.click_on_search_icon()


@then("Verify {search_result} is on Amazon Page")
def is_search_matching(context, search_result):
    context.app.search_result_page.verify_search_result(search_result)


@then("Verify url contains {search_query}")
def is_url(context, search_query):
    context.app.search_result_page.verify_url_contains(search_query)


@then('Verify Cart has {num} items in it')
def is_num_items(context, num):
    find_the_cart = context.driver.find_element(*ITEMS_IN_CART).text  # using XPath hence CSS no good with text linking
    assert int(num) == int(find_the_cart), f"Expected num of items was {num}, but the actual is {find_the_cart}"
