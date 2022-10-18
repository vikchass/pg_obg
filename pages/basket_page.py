from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST_FORM), "Basket is not empty"

    def should_be_products_in_basket(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_LIST_FORM), "Basket is empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text is not present"

    def should_not_displayed_empty_basket_text(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text displayed"