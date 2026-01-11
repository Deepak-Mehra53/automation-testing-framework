from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
import time

def test_logout(setup):
    driver = setup

    login = LoginPage(driver)
    login.open()
    login.enter_email("testcase1234@gmail.com")
    login.enter_password("Test@123")
    login.click_login()

    time.sleep(2)

    logout = LogoutPage(driver)
    logout.click_logout()

    assert logout.is_logged_out()
