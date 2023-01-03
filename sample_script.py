from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# we are going to initiate driver
start_chrome = Service('C:\\Users\\Buywi\\Desktop\\QA Automation Practice\\'
                       'Python_Amazon_Automation\\chromedriver.exe')
driver = webdriver.Chrome(executable_path=start_chrome)
driver.maximize_window()


# we are going to give url to our driver
driver.get('https://google.com')

# search in search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# we are waiting for 4 seconds
sleep(4)

# select the search button
driver.find_element(By.NAME, 'btnK').click()

# let's verify our result

assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text

# close chrome
driver.quit()












num = 84434374433

num_2 = 0

while num > 10:
    num_2 = num % 10
    num //= 10
print(num_2)