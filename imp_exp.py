from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# implicit wait 100ms 1/10 of second
# explicit wait 500ms 1/2 of second
# to turn off implicit, call it again with 0

start_chrome = Service('/Users/mikesoloman/Desktop/Python_Amazon_Automation/chromedriver')
driver = webdriver.Chrome(service=start_chrome)
driver.maximize_window()

# driver.get("https://www.google.com")
#
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys("Dress")

driver.wait = WebDriverWait(driver, 10)
# e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# e.click()

# driver.get("https://www.amazon.com/MEROKEETY-Womens-Flutter-Sleeve-S"
#            "mocked/dp/B09X46V8V7/ref=sr_1_6?crid=2EGZ53F1V4EC5&keywo"
#            "rds=dress&qid=1664575257&qu=eyJxc2MiOiIxMy4wOSIsInFzYSI6I"
#            "jEzLjI0IiwicXNwIjoiMTIuMjgifQ%3D%3D&sprefix=dress%2Caps%2C90&sr=8-6")
#
# colors = driver.find_elements(*(By.CSS_SELECTOR, "#twister li"))
# expected_list = ["Armygreen", "Beige", "Black", "Coffee", "Darkpink", "Dustyblue", "Dustypink", "Forestgreen", "Ginger", "Lightblue",
#                  "Navy", "Orange", "Purple", "Rust", "Sage", "Watermelon", "White", "Wine", "Pearl White"]
# for i in range(len(colors)):
#     colors[i].click()
#     actual = driver.find_element(*(By.XPATH, "//div[@id='variation_color_name'] // span[@class='selection']")).text
#     print(actual)
#     print(expected_list[i])
#     assert expected_list[i] == actual, f"{expected_list[i]} was expected, but got {actual} instead"

driver.get("https://www.amazon.com/dp/B081YS2F7N")

colors = driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

for color in colors:
    color.click()
    print(driver.find_element(By.XPATH, "//div[@id = 'variation_color_name'] // span[@class='selection']").text)
