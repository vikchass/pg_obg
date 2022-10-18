from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, e, et):
        # self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()
        self.register_new_user(e, et)

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Cant find word login in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутсвует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "Форма регистрации отсутсвует"

    def register_new_user(self, email, password):
        email.is_element_present(*ProductPageLocators.EMAIL)
        email.send_key("rodionova.victory@yandex.ru")
        password.is_element_present(*ProductPageLocators.PASSWORD1)
        password.send_key("Qq123")
        password.is_element_present(*ProductPageLocators.PASSWORD2)
        password.send_key("Qq123")

