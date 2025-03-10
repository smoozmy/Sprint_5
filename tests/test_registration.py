from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestRegistration:
    def test_successful_registration(self, driver, user):
        page = RegistrationPage(driver)
        page.open()
        page.register(user['username'], user['email'], user['password'])

        assert driver.current_url == LoginPage.URL

    def test_failed_registration_empty_name(self, driver, user):
        page = RegistrationPage(driver)
        page.open()
        page.register('', user['email'], user['password'])

        assert driver.current_url == RegistrationPage.URL

    def test_failed_registration_short_password(self, driver, user):
        page = RegistrationPage(driver)
        page.open()
        page.register(user['username'], user['email'], '12345')

        error_text = page.get_error_message()

        assert error_text == 'Некорректный пароль'