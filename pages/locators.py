from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTR_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTR_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REP_REGISTR_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    CART_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button[type='submit']")
    CART_MESSAGE = (By.CSS_SELECTOR, "div#messages strong")
    BOOK_TITLE = (By.CSS_SELECTOR, "div.content h1")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1)")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, "#basket_totals .total")
