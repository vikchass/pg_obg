from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_success_message(self, product_title: str):
        assert product_title == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def should_be_price_message(self, product_price: str):
        assert product_price == self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

    def get_product_title(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

