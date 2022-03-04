from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)        
    
    def should_not_be_total_basket(self):
    	assert self.is_not_element_present(*MainPageLocators.BASKET_TOTAL), "Basket not empty!!!"
