from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#registration_link")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_1 = (By.CLASS_NAME, "btn-add-to-basket")
    TEXT_1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    TEXT_2 = (By.TAG_NAME, "h1")
    PRICE_1 = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_2 = (By.CLASS_NAME, "price_color")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")





