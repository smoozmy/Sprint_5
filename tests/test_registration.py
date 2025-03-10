import pytest

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.data import username
from utils.generators import generate_email, generate_password


class TestRegistration():
    def test_successful_registration(self, driver):
        page = RegistrationPage(driver)
        page.open()
        page.register(username, generate_email(), generate_password())

        assert driver.current_url == LoginPage.URL

    def test_failed_registration_empty_name(self, driver):
        page = RegistrationPage(driver)
        page.open()
        page.register('', generate_email(), generate_password())

        assert driver.current_url == RegistrationPage.URL

    def test_failed_registration_short_password(self, driver):
        page = RegistrationPage(driver)
        page.open()
        page.register(username, generate_email(), '12345')

        error_text = page.get_error_message()

        assert error_text == 'Некорректный пароль'