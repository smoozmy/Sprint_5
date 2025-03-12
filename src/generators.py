import random
import string
from src.data import User


def generate_email():
    return f'krapivin19{random.randint(100, 999)}@ya.ru'

def generate_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_user():
    return User(
        name="Тестовый Пользователь",
        email=generate_email(),
        password=generate_password()
    )