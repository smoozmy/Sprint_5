from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    LOGIN_PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
    LOGIN_TITLE = By.XPATH, '//h2[text()="Вход"]'

class RegistrationLocators:
    REGISTER_NAME_INPUT = By.XPATH, '(//input[@name="name"])[1]'
    REGISTER_EMAIL_INPUT = By.XPATH, '(//input[@name="name"])[2]'
    REGISTER_PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'
    REGISTER_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]'
    ERROR_MESSAGE = By.XPATH, '//p[text()="Некорректный пароль"]'
    LOGIN_PAGE_BUTTON = By.XPATH, '//a[contains(@class, "Auth_link")]'
    REGISTRATION_TITLE = By.XPATH, '//h2[text()="Регистрация"]'

class ConstructorLocators:
    LOGIN_PAGE_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'

class ForgotPasswordLocators:
    LOGIN_PAGE_BUTTON = By.XPATH, '//a[text()="Войти"]'