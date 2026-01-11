from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

def test_place_order_flow(setup):
    driver = setup


    login = LoginPage(driver)
    login.open()
    login.enter_email("testcase1234@gmail.com")
    login.enter_password("Test@123")
    login.click_login()


    product = ProductPage(driver)
    product.add_first_product_to_cart()
    product.click_view_cart()


    checkout = CheckoutPage(driver)
    checkout.click_checkout()
    checkout.get_address_text()


    payment = PaymentPage(driver)
    payment.fill_card()
    payment.click_pay()


    assert payment.is_success()
