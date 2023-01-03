from matplotlib.dviread import Page
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from sympy import product
from app.application import Application
import HtmlTestRunner
from selenium.webdriver.support import expected_conditions as EC 
def document_initialised(driver):
    return driver.execute_script("return initialised")
def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path= "/amazon_selenium_automatio"
                                                       "n_Page_Object_Model/chromedriver")
    
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    context.driver.save_screenshot('./before {step}.png')
    context.driver.implicitly_wait(2)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.save_screenshot('./before quit.png')
    context.driver.quit()
    print("selesai")
    