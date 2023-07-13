from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def product_name_must_be_the_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alert_inner_product_name = self.browser.find_element(*ProductPageLocators.ALERT_INNER_PRODUCT_NAME)
        assert product_name.text == alert_inner_product_name.text, "The product name must be the same in the description and purchase notification."

    def price_must_be_the_same(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        alert_info_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO_PRICE)
        assert price.text == alert_info_price.text, "The price must be the same in the description and purchase notification."




