from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        login_url = LoginPageLocators.LOGIN_URL
        assert login_url in current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "Register form is not presented"

    def register_new_user(self, email, password):
        browser = self.browser
        email_field = browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field_1 = browser.find_element(*LoginPageLocators.PASSWORD_FIELD_1)
        password_field_1.send_keys(password)
        password_field_2 = browser.find_element(*LoginPageLocators.PASSWORD_FIELD_2)
        password_field_2.send_keys(password)
        button_registration = browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE_REGISTRATION), "Fail registration"



