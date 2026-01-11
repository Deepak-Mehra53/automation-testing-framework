from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def open_products(self):
        self.driver.get("https://automationexercise.com/products")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 600)")
        time.sleep(2)

    def add_first_product_to_cart(self):
        self.scroll_down()


        product = self.driver.find_element(By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
        self.actions.move_to_element(product).perform()
        time.sleep(1)


        add_to_cart = self.driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")


        self.driver.execute_script("arguments[0].click();", add_to_cart)

    def click_view_cart(self):
        time.sleep(2)
        view_cart = self.driver.find_element(By.XPATH, "//u[text()='View Cart']")
        view_cart.click()
