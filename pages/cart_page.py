from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)

    def is_item_in_cart(self, item_name):
        # Wait for cart items to be present and check if the specified item is in the cart
        items = self.wait.until(lambda driver: driver.find_elements(*self.CART_ITEMS))
        for item in items:
            name_element = item.find_element(*self.ITEM_NAME)
            if item_name in name_element.text:
                return True
        return False
