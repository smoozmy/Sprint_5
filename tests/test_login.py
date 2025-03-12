from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import LOGIN_URL, TEST_USER, REGISTER_URL, CONSTRUCTOR_URL, FORGOT_PASSWORD_URL, PROFILE_URL
from src.locators import LoginLocators, ConstructorLocators, RegistrationLocators, ForgotPasswordLocators


class TestLogin:
    def test_login_from_login_page(self, driver):
        driver.get(LOGIN_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'

    def test_login_from_registration_page(self, driver):
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            RegistrationLocators.LOGIN_PAGE_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'

    def test_login_from_constructor_page(self, driver):
        driver.get(CONSTRUCTOR_URL)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ConstructorLocators.LOGIN_PAGE_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'

    def test_login_from_forgot_page(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ForgotPasswordLocators.LOGIN_PAGE_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'

    def test_login_from_profile_page(self, driver):
        driver.get(PROFILE_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'