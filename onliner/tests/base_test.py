import logging
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_test import TestLogInPage


class BaseTest(unittest.TestCase):

    def setUp(self):

        # logger = logging.getLogger(__name__)
        # logging.basicConfig(
        #     level=logging.INFO,
        #     style="{",
        #     format='[{levelname:1.1} {asctime} {module}:{lineno}] {message}',
        #     datefmt='%y%m%d %H:%M:%S',
        # )

        options = Options()
        options.add_argument("--headless")
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        # options.add_argument("--start-fullscreen")
        # options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://www.onliner.by/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogInPage)
    unittest.TextTestRunner(verbosity=1).run(suite)
