from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    def is_logged_out(self):
        try:
            return self.driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").is_displayed()
        except:
            return False
