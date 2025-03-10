from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.data import BASE_URL, PATCH_REGISTER


class RegistrationPage(BasePage):
    URL = BASE_URL + PATCH_REGISTER

    NAME_INPUT = (By.XPATH, '(//input[@name="name"])[1]')
    EMAIL_INPUT = (By.XPATH, '(//input[@name="name"])[2]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]')

    def open(self):
        self.driver.get(self.URL)

    def register(self, name, email, password):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.REGISTER_BUTTON)

    def get_error_message(self):
        return self.get_element(self.ERROR_MESSAGE).text