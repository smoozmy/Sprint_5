from utils.generators import generate_email, generate_password

BASE_URL = 'https://stellarburgers.nomoreparties.site/'

PATCH_REGISTER = 'register'
PATCH_LOGIN = 'login'

username = 'Тестовый Пользователь'
email = generate_email()
password = generate_password()