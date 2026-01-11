from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def open(self):
            self.driver.get("https://automationexercise.com/login")

    def enter_email(self, email):
            self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)

    def enter_password(self, password):
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

    def click_login(self):
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def is_user_logged_in(self):
        try:
            return self.driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").is_displayed()
        except:
            return False