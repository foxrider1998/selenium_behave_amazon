from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

HOME_PAGE = "https://www.amazon.com/"
SIGN_IN_POPUP = (By.CSS_SELECTOR, "div.nav-signin-tt.nav-flyout a.nav-action-button")
DIV_WHOLE_FOODS = (By.XPATH, "//div[@data-toaster-blocking = 1]")
CLICK_TO_CLOSE = (By.CSS_SELECTOR, "span.a-button-inner input[data-action-type='DISMISS']")
PRODUCTS_ON_PAGE = (By.XPATH, '//li[contains(@class, "result-item")] //div[contains(@class, "edium a-padding-none '
                              'a-text-left")]')
DESC_OF_ITEMS = (By.CSS_SELECTOR, 'div.s-item-container span[class*= "product-name a-text-bold"]')
WHOLE_FOODS_DEALS = "https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz"


@given('Amazon Home Page')
def go_to_home(context):
    context.driver.get(HOME_PAGE)


@then("Verify Sign_IN is clickable")
def is_sign_in_there(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))


@when("Verify SIGN_IN Popup is still there for {seconds}")
def is_popup_gone(context, seconds):
    sleep(int(seconds))


@then("Verify Sign_in disappears")
def is_sign_in_gone(context):
    context.driver.wait.until(EC.invisibility_of_element(SIGN_IN_POPUP))


@when("Navigate to the given {dress_page}")
def go_to_the_page(context, dress_page):
    context.driver.get(dress_page)


@then("Verify {expected_colors} matching Actual Colors for the item")
def is_colors_match(context, expected_colors):
    expected_colors = expected_colors.split("; ")
    print(expected_colors)
    colors = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")
    index = 0
    for color in colors:
        color.click()
        actual = context.driver.find_element(By.XPATH,
                                             "//div[@id = 'variation_color_name'] // span[@class='selection']").text
        print(actual)
        print(expected_colors[index])
        assert actual == expected_colors[index], f"Expected was {expected_colors[index]}, but we got {actual}"
        index += 1


@given("Whole Foods Amazon Deals")
def whole_foods(context):
    context.driver.get(WHOLE_FOODS_DEALS)


@when("If there is a popup, Close the Whole Foods is not available for this location popup")
def is_popup_whole_food(context):
    if len(context.driver.find_elements(*DIV_WHOLE_FOODS)) == 1:
        context.driver.find_element(*CLICK_TO_CLOSE).click()


@then("Verify items have {expected_word} and item has a Name/Description")
def is_regular_product_name(context, expected_word):
    # context.driver.wait.until(EC.text_to_be_present_in_element(PRODUCTS_ON_PAGE, expected_word))
    list_of_items = context.driver.find_elements(*PRODUCTS_ON_PAGE)
    for item in list_of_items:
        assert expected_word in item.text, f"Expected word {expected_word} is not in item {item}"
        item_description = item.find_element(*DESC_OF_ITEMS)
        print(item_description.text)
        assert item_description.text, f"Error, Product name is missing"
