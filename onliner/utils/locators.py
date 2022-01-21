from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGO = (By.CLASS_NAME, "onliner_logo")
    LOGIN_BUTTON = (By.CLASS_NAME, "//div[contains(text(),'Вход')]")


class LoginPageLocators(object):
    LOGIN_CHECK = (By.CLASS_NAME, "//div[contains(text(),'Через социальные сети')]")
    LOGIN_EMAIL = (By.XPATH, "//input[@type='text']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[@type='submit']")
    USER_PROFILE = (By.CLASS_NAME, "b-top-profile__image js-header-user-avatar")
