from src.data import REGISTER_URL
from src.locators import RegistrationLocators, LoginLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_successful_registration(self, driver, user):
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_NAME_INPUT)).send_keys(user.name)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_EMAIL_INPUT)).send_keys(user.email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_PASSWORD_INPUT)).send_keys(user.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            RegistrationLocators.REGISTER_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_TITLE)).text == 'Вход'

    def test_failed_registration_empty_name(self, driver, user):
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_NAME_INPUT)).send_keys('')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_EMAIL_INPUT)).send_keys(user.email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_PASSWORD_INPUT)).send_keys(user.password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            RegistrationLocators.REGISTER_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTRATION_TITLE)).text == 'Регистрация'

    def test_failed_registration_short_password(self, driver, user):
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_NAME_INPUT)).send_keys(user.name)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_EMAIL_INPUT)).send_keys(user.email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.REGISTER_PASSWORD_INPUT)).send_keys('12345')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            RegistrationLocators.REGISTER_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            RegistrationLocators.ERROR_MESSAGE)).text == 'Некорректный пароль'