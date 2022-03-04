from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_total_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), "Basket not empty!!!"
