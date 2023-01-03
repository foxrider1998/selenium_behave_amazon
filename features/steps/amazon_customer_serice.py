from selenium.webdriver.common.by import By
from behave import given, when, then

MY_BOXES = (By.CSS_SELECTOR, "div[class*=_p13n-zg-nav-tab-all_style_zg-tabs-l")
ACTUAL_GREETING = (By.XPATH, "//div[@class='page-container'] //h1")
CUST_BOXES = (By.CSS_SELECTOR, "div.issue-card-container div.issue-card-wrapper")
LIB_TEXT = (By.XPATH, "//label // h2")
LIB_SEARCH_BAR = (By.XPATH, "//input[@id='hubHelpSearchInput']")
LIB_BOX_COUNT = (By.CSS_SELECTOR, "div.article-wrapper.active div[role=button]")
IS_HELP_TEXT = (By.XPATH, "//div[@class='page-wrapper'] // h2")



@given("Go to Best Seller's Page")
def go_to_best_sellers_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/")


@when('Count Best Sellers Nav Boxes')
def count_boxes(context):
    my_boxes_count = context.driver.find_elements(*MY_BOXES)
    print(len(my_boxes_count))


@then("Verify there are {num} boxes")
def is_boxes(context, num):
    actual = context.driver.find_elements(*MY_BOXES)
    assert int(num) == len(actual), f"Expected num of boxes was: {num} but the actual amount is {actual}"


@given("Go to Customer Service Page")
def go_cust_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@then("Verify {text} is present")
def is_greeting(context, text):
    actual_text = context.driver.find_element(*ACTUAL_GREETING).text
    assert text == actual_text, f"Expected text was {text}, but we got {actual_text}"


@then("Verify {num} amount of boxes underneath of Greeting text")
def is_amount_cust(context, num):
    actual_num = len(context.driver.find_elements(*CUST_BOXES))
    print(actual_num)
    assert int(num) == actual_num, f"Wrong amount of boxes, expected was {num}, but we got {actual_num}"


@then("Confirm {library_text} is about Library Search Box")
def is_lib_text(context, library_text):
    actual_text = context.driver.find_element(*LIB_TEXT).text
    assert library_text == actual_text, f"Wrong text, expected text was {library_text}, but the actual is {actual_text}"


@then("Verify Library Search Bar is there")
def is_lib_search_bar(context):
    context.driver.find_element(*LIB_SEARCH_BAR)


@then("Verify {num_lib} boxes are there")
def lib_boxes(context, num_lib):
    actual_count = len(context.driver.find_elements(*LIB_BOX_COUNT))
    print(actual_count)
    assert int(num_lib) == actual_count, f"expected num was{num_lib} but we got {actual_count}"


@then("Verify {help} text")
def is_help_text(context, help):
    actual_text = context.driver.find_elements(*IS_HELP_TEXT)[1].text
    print(actual_text)
    assert help == actual_text, f"Actual text is {actual_text}"
