from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        basket_url = BasketPageLocators.BASKET_URL
        assert basket_url in current_url, "Basket url is not presented"

    def guest_can_see_basket_form_with_products(self):
        basket_form = self.is_element_present(*BasketPageLocators.BASKET_FORM)
        assert basket_form, "Basket form is empty"

    def guest_can_not_see_basket_form_with_products(self):
        basket_form = self.is_not_element_present(*BasketPageLocators.BASKET_FORM)
        assert basket_form, "Basket form is not empty"

    def should_not_be_message_about_empty_basket(self):
        content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        text = content.text
        assert "Your basket is empty." not in text, "Basket is empty"

    def should_be_message_about_empty_basket(self):
        content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        text = content.text
        assert "Your basket is empty." in text, "Basket is not empty"







