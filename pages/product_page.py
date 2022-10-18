import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button()
        self.should_be_text()
        # self.should_be_price()

    def should_be_product_page2(self):
        self.should_not_be_success_message()

    def should_be_button(self):
        self.is_element_present(*ProductPageLocators.BUTTON_1)
        self.solve_quiz_and_get_code()

    def should_be_text(self):
        assert self.is_element_text(*ProductPageLocators.TEXT_1) == self.is_element_text(*ProductPageLocators.TEXT_2)

    def should_be_price(self):
        assert self.is_element_text(*ProductPageLocators.PRICE_1) == self.is_element_text(*ProductPageLocators.PRICE_2)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_1), \
            "Success message is presented, but should not be"

