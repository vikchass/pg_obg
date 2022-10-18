from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/accounts/login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, username: str, password: str):
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT).click()