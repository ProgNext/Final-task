from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
            "Button add to basket is not presented!"

    def should_be_elements_for_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), \
            "Name product is not presented!"
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), \
            "Price product is not presented!"

    def should_be_elements_for_alert_inner(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_IN_ALERTINNER), \
            "Name product in alert inner is not presented!"
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_IN_ALERTINNER), \
            "Price product in alert inner is not presented!"

    def ckeck_data_product_and_alert_inner(self):
        nameProduct = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        nameProductInAlertInner = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERTINNER).text
        priceProduct = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        priceProductInAlertInner = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_ALERTINNER).text
        self.s1_equals_s2(nameProduct, nameProductInAlertInner)
        self.s1_equals_s2(priceProduct, priceProductInAlertInner)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is not disappeared"

