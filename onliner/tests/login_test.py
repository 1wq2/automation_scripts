import unittest
import os
from base_test import BaseTest
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage


class TestLogInPage(BaseTest):

    def setUp(self):
        super(TestLogInPage, self).setUp()

    def test_login_button(self):
        page = MainPage(self.driver)
        page.click_login_button()

    def test_login_page(self):
        page = LoginPage(self.driver)

        ONL_EMAIL, ONL_PASS = os.getenv('ONL_EMAIL'), os.getenv('ONL_PASS')
        if not ONL_EMAIL or not ONL_PASS:
            # logger.error
            print('Onliner''s email and/or password environment variables could not be imported.')
            raise Exception

        self.assertIn('социальные', page.check_login_page().textContent)

        page.enter_email(ONL_EMAIL)
        page.enter_password(ONL_PASS)
        page.click_login_button()

        self.assertTrue(page.check_user_profile())

    def tearDown(self):
        super(TestLogInPage, self).tearDown()
