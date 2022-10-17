from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button()

    def should_be_button(self):
        self.is_element_present(*ProductPageLocators.BUTTON_1)
        self.solve_quiz_and_get_code()


