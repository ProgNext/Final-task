from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_elements_for_product()
    page.should_be_elements_for_alert_inner()
    page.ckeck_data_product_and_alert_inner()