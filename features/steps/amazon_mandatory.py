from selenium.webdriver.common.by import By
from behave import given, when, then

from selenium.webdriver.support.wait import WebDriverWait

AMAZON_HOME_PAGE = 'https://www.amazon.com'
SEARCH_BAR = (By.CSS_SELECTOR, "form#nav-search-bar-form input[type='text']")
SEARCH_ICON = (By.CSS_SELECTOR, "div.nav-right input[class*='rogressive-att']")
SEARCH_RESULT = (By.XPATH, "//div[@class='sg-col-inner']//span[contains(@class, 'tate a-text-bold')]")
ITEMS_IN_CART = (By.XPATH, "//div[@id='nav-cart-count-container']/ span[@id='nav-cart-count']")




@when("Select categorie electronics")
def search_for_Tvs(context):
    context.app.main_page.click_on_All()
    context.app.main_page.click_on_shop_by_dep_elc()
    context.app.main_page.click_on_elc_tv()

# @then("Choose Tv&Video")
# def click_on_shop_by_dep_elc(context):


@then("Sort by price")
def click_sort_by_price_(context):
    context.app.search_result_page.search_for_tv()
    context.app.search_result_page.criteria_Under_32_in()
    context.app.search_result_page.sort_by_desc()
    context.app.search_result_page.filteringbyBpoint()
    
    
    




