from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time

def before_all(context):
    # Get delay from userdata, default to 0 if not specified
    context.delay = float(context.config.userdata.get('DELAY', '0'))
    
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    
    # Initialize the driver
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    
    # Initialize page objects
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)

def after_all(context):
    # Clean up after all tests
    context.driver.quit()

def after_scenario(context, scenario):
    # Clean up after each scenario
    context.driver.delete_all_cookies()

def before_step(context, step):
    # Add delay before each step if specified
    if hasattr(context, 'delay') and context.delay > 0:
        time.sleep(context.delay)
