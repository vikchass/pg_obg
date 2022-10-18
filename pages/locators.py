from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#registration_link")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_1 = (By.CLASS_NAME, "btn-add-to-basket")
    # SUCCESS_MESSAGE = "*****" \
    TEXT_1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    TEXT_2 = (By.TAG_NAME, "h1")
    PRICE_1 = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_2 = (By.CLASS_NAME, "price_color")
#
#
#
#
# был добавлен в вашу корзину
# Ваша корзина удовлетворяет условиям
# предложения





