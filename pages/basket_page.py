from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators
import pytest

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_message_basket_empty()
        self.should_be_basket_empty()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'basket' in self.browser.current_url, \
            "This page isn't Basket-Page!"

    def should_be_message_basket_empty(self):
        # реализуйте проверку, что присутствует надпись "Ваша корзина пуста"
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "Message is not presented!"

    def should_be_basket_empty(self):
        # реализуйте проверку, что корзина пуста
        assert not self.is_element_present(*BasketPageLocators.BASKET_FULL), \
            "Basket is not empty!"


    def should_not_be_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "Success message is presented, but should not be"
