from pages.login_page import LoginPage

def test_login_page(setup):
    driver = setup

    login = LoginPage(driver)
    login.open()

    login.enter_email("testcase1234@gmail.com")
    login.enter_password("Test@123")
    login.click_login()

    assert login.is_user_logged_in()