
from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class SearchResultPage(Page):

    SEARCH_RESULT = (By.XPATH, "//div[@class='sg-col-inner']//span[contains(@class, 'tate a-text-bold')]")
    TELEVISIONS_cat= (By.XPATH, "//span[.='Televisions']")
    UNDER_32_IN= (By.XPATH, "//span[.='32 Inches & Under']")
    HTLsort= (By.XPATH, "//a[.='Price: High to Low']")
    sortBtn = (By.ID,"s-result-sort-select")
    Under32_by_link= (By.LINK_TEXT, "32 inches & under")
    
    
    
    
    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.SEARCH_RESULT)
        
    def search_for_tv(self):
        self.click(*self.TELEVISIONS_cat) 

    def criteria_Under_32_in(self):
        self.scroll_to(*self.UNDER_32_IN)
        self.click(*self.UNDER_32_IN)
        sleep(4)
        
    def sort_by_desc(self):
        
        sort_dropdown = self.driver.find_element(By.ID, "s-result-sort-select")
        desc=sort_dropdown.find_element(By.XPATH, "//option[@value='price-desc-rank']").click()
        # self.click(desc)
        sleep(6)
        
        
    def addingproducts(self):    
        product_containers = self.driver.find_elements(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section")
        
        for container in product_containers:
            name = container.find_element(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(11) > div > div > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2").text
            price = container.find_element(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(11) > div > div > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-price-instructions-style > div > a > span > span:nth-child(2) > span.a-price-whole").text
            product ={name,price}
            self.save_products(product)    
     
    def filteringbyBpoint(self):
         #  # filter model year 2017
        modelYear = self.driver.find_element("xpath","//li[contains(.,'2017')]")
        ActionChains(self.driver)\
            .scroll_to_element(modelYear)\
            .perform()
        modelYear.click()    
        # filter under $150
        highPriceBox = self.driver.find_element(By.ID,"high-price")
        self.driver.save_screenshot('./4hightolow.png')  
        highPriceBox.clear()
        highPriceBox.send_keys("150")
        highPriceBox.send_keys(Keys.RETURN)
   