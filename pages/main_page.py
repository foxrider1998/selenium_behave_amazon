from pages.base_page import Page
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait


class MainPage(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, "form#nav-search-bar-form input[type='text']")
    SEARCH_ICON = (By.CSS_SELECTOR, "div.nav-right input[class*='rogressive-att']")
    ALL_BUTTON= (By.XPATH, "//span[@class='hm-icon-label']")
    SHOPBYDEP_ELC= (By.CSS_SELECTOR, "[data-ref-tag='nav_em_1_1_1_6']")
    SIDEBAR= (By.ID, "leftNavContainer")
    ELC_tv_bylinktext = (By.LINK_TEXT, "Television & Video")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    # ALL_BUTTON= ('xpath', "")
    def open_main_page(self):
        self.open_page('https://www.amazon.com')

    def input_amazon_search(self, text):
        self.input_text(text, *self.SEARCH_FIELD)

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)
        
    def click_on_All(self):
        self.click(*self.ALL_BUTTON)    
        
    def click_on_shop_by_dep_elc(self):
        self.click(*self.SHOPBYDEP_ELC)     
        
    def click_on_elc_tv(self):
        self.scroll_to(*self.ELC_tv_bylinktext)
        self.click(*self.ELC_tv_bylinktext)
        print("End of main page")
