import pytest
import time
import math    
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.go_to_login_page() 
    time.sleep(2)    
    page.solve_quiz_and_get_code()        
    
   
