from base_page import BasePage
from login_page import LoginPage
from ..utils.locators import *


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver) 

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()
        return LoginPage(self.driver)
