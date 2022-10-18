from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize('param', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.parametrize('param', ["0"])
def test_user_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


def test_user_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page2()


link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.fixture(scope="function")
def test_register_new_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.should_be_authorized_user()

    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):





















