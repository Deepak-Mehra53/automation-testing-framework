from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()

    def click_checkout(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']").click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 600)")
        time.sleep(2)


    def get_address_text(self):
        self.scroll_down()
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn-default.check_out").click()
