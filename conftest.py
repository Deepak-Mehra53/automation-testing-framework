import pytest
from selenium import webdriver
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    email = f"deepak{int(time.time())}@gmail.com"
    return email
