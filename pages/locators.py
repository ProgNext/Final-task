from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_FULL = (By.CSS_SELECTOR, "basket-title hidden-xs")


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_PRODUCT_IN_ALERTINNER = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_PRODUCT_IN_ALERTINNER = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alert-success")
