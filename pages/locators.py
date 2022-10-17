from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#registration_link")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")

