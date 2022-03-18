from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_FULL = (By.CSS_SELECTOR, "basket-title hidden-xs")


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_PRODUCT_IN_ALERTINNER = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_PRODUCT_IN_ALERTINNER = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alert-success")
