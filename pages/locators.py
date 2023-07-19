from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    ALERT_INNER_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main h1")
    ALERT_INFO_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SUCCESS_MESSAGE_REGISTRATION = ((By.CSS_SELECTOR, ".alert.alert-success"))

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    BASKET_URL = "basket"
    BASKET_TITLE = (By.CSS_SELECTOR, ".page-header.action")
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")

