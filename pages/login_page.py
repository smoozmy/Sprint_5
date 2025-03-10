from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.data import BASE_URL, PATCH_LOGIN


class LoginPage(BasePage):
    URL = BASE_URL + PATCH_LOGIN

    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')

