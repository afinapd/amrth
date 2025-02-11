from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage(BasePage):
    # Locators
    CART_LINK = (By.XPATH, '//div[@id="shopping_cart_container"]/a')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    ABOUT_LINK = (By.ID, 'about_sidebar_link')
    TEXT_TITLE = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self, item_name):
        # Locate the button for the item and click it to add to cart
        button_id = f'add-to-cart-{item_name.lower().replace(" ", "-")}'
        item_button = self.find_clickable_element(By.ID, button_id)
        item_button.click()

    def open_cart(self):
        self.find_clickable_element(*self.CART_LINK).click()
        time.sleep(2)

    def get_cart_count(self):
        try:
            return self.find_element(*self.CART_BADGE).text
        except:
            return "0"

    def click_hamburger_menu(self):
        self.find_clickable_element(*self.BURGER_MENU).click()
        self.wait.until(EC.element_to_be_clickable(self.ABOUT_LINK))

    def click_about_link(self):
        self.find_clickable_element(*self.ABOUT_LINK).click()

    def get_current_url(self):
        self.wait.until(lambda driver: "saucelabs.com" in driver.current_url)
        return self.driver.current_url
