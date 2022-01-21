from ..utils.locators import *
from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def check_login_page(self):
        self.find_element(*self.locator.LOGIN_CHECK)

    def enter_email(self, email):
        self.find_element(*self.locator.LOGIN_EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.LOGIN_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_SUBMIT).click()

    def check_user_profile(self):
        return True if self.find_element(*self.locator.USER_PROFILE) else False

