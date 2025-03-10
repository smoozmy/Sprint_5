import pytest
from pages.registration_page import RegistrationPage


class TestRegistration():
    def test_open_registration_page(self, driver):
        page = RegistrationPage(driver)
        page.open()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'