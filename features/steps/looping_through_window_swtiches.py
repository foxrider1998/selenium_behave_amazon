from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


BEST_PAGE = "https://www.amazon.com/Best-Sellers/zgbs/ref=zg_mg_tab"
MY_LINKS = (By.XPATH, "// div[@id='zg_header'] // a")


@given("Open Amazon Best Seller Page")
def best_page(context):
    context.driver.get(BEST_PAGE)


@then("Verify {text_1} is on page")
def is_text1(context, text_1):
    context.my_links = context.driver.find_elements(*MY_LINKS)
    print(context.my_links[0].text)
    assert text_1 in context.my_links[0].text, f"Expected text {text_1} is not in {context.my_links[0].text}"


@when("Loop through links and verify")
def is_text_matches(context):
    context.my_links = context.driver.find_elements(*MY_LINKS)
    expected_text = ["Best Sellers","New Releases", "Movers & Shakers", "Most Wished For", "Gift Ideas"]
    for char in range(len(context.my_links)):
        link = context.driver.find_elements(*MY_LINKS)[char]
        link_text = link.text
        link.click
        print(link_text)
        print(expected_text[char])
        assert expected_text[char] in link_text, f"expected text was {expected_text}, but we got {link_text}"
