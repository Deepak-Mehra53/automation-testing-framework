from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_product_added(self):
        product = self.driver.find_element(By.CLASS_NAME, "cart_info")
        return product.is_displayed()
