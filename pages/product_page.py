from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def go_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart_button.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), "Cart button is not presented!!!"

    def is_product_in_cart(self):
        product_cart = self.browser.find_element(*ProductPageLocators.CART_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert product_cart == product_name, "Not valid product in cart!!!"

    def is_price_book_cart(self):
        price_cart = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        price_product = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert price_cart == price_product, "Not valid price in cart!!!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be!!!"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message does not disappear!!!"
