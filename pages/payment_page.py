from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_card(self):
        self.driver.find_element(By.NAME, "name_on_card").send_keys("Deepak")
        self.driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
        self.driver.find_element(By.NAME, "expiry_year").send_keys("2030")

    def click_pay(self):
        self.driver.find_element(By.ID, "submit").click()

    def is_success(self):
        try:
            return self.driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations')]").is_displayed()
        except:
            return False
