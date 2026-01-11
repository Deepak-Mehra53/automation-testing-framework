from selenium.webdriver.common.by import By

class AccountInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def select_title(self):
        self.driver.find_element(By.ID, "id_gender1").click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def select_dob(self):
        self.driver.find_element(By.ID, "days").send_keys("10")
        self.driver.find_element(By.ID, "months").send_keys("January")
        self.driver.find_element(By.ID, "years").send_keys("1999")

    def fill_address(self):
        self.driver.find_element(By.ID, "first_name").send_keys("Deepak")
        self.driver.find_element(By.ID, "last_name").send_keys("Mehra")
        self.driver.find_element(By.ID, "company").send_keys("TestCompany")
        self.driver.find_element(By.ID, "address1").send_keys("Delhi Street")
        self.driver.find_element(By.ID, "country").send_keys("India")
        self.driver.find_element(By.ID, "state").send_keys("Delhi")
        self.driver.find_element(By.ID, "city").send_keys("Delhi")
        self.driver.find_element(By.ID, "zipcode").send_keys("110011")
        self.driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

    def click_create_account(self):
        self.driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

