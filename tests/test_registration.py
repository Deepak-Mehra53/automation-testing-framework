from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
import time

def test_user_registration(setup, new_user):
    driver = setup


    signup = SignupPage(driver)
    signup.open()
    signup.enter_name("Deepak")
    signup.enter_email(new_user)
    signup.click_signup()


    account = AccountInfoPage(driver)
    account.select_title()
    account.enter_password("Test@123")
    account.select_dob()
    account.fill_address()
    account.click_create_account()
    time.sleep(2)


    assert "Account Created!" in driver.page_source
