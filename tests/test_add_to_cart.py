from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time

def test_add_to_cart(setup):
    driver = setup


    login = LoginPage(driver)
    login.open()
    login.enter_email("testcase1234@gmail.com")
    login.enter_password("Test@123")
    login.click_login()


    product = ProductPage(driver)
    product.open_products()


    product.add_first_product_to_cart()
    time.sleep(5)
    product.click_view_cart()


    cart = CartPage(driver)
    assert cart.verify_product_added() == True
