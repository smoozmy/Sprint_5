from src.data import LOGIN_URL, TEST_USER
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import LoginLocators, ProfileLocators, ConstructorLocators


class TestProfile:
    def test_go_to_profile_after_login(self, driver):
        driver.get(LOGIN_URL)

        # Авторизация
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        # Переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ProfileLocators.PROFILE_PAGE_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ProfileLocators.PROFILE_TAB_LABEL)).text == 'Профиль'

    def test_go_to_constructor(self, driver):
        driver.get(LOGIN_URL)

        # Авторизация
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        # Переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ProfileLocators.PROFILE_PAGE_BUTTON)).click()

        # Переход в конструктор
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ConstructorLocators.LOGO_STELLAR_BURGER)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstructorLocators.ORDER_BUTTON)).text == 'Оформить заказ'

    def test_logout(self, driver):
        driver.get(LOGIN_URL)

        # Авторизация
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_EMAIL_INPUT)).send_keys(TEST_USER["email"])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_PASSWORD_INPUT)).send_keys(TEST_USER["password"])
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON)).click()

        # Переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ProfileLocators.PROFILE_PAGE_BUTTON)).click()

        # Переход в конструктор
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            ProfileLocators.LOGOUT_TAB_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            LoginLocators.LOGIN_TITLE)).text == 'Вход'

