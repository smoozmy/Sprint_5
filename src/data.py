from dataclasses import dataclass

BASE_URL = 'https://stellarburgers.nomoreparties.site'

LOGIN_URL = f'{BASE_URL}/login'
REGISTER_URL = f'{BASE_URL}/register'
CONSTRUCTOR_URL = BASE_URL
FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
PROFILE_URL = f'{BASE_URL}/account'


@dataclass
class User:
   name: str
   email: str
   password: str

TEST_USER = {
    "username": "Александр Крапивин",
    "email": "akrapivin19123@yandex.ru",
    "password": "TestPass123"
}

