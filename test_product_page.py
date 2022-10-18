from .pages.product_page import ProductPage
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('param', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


# def should_not_be_success_message(self):
#     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#        "Success message is presented, but should not be"


















