import random
import string


def generate_email():
    return f'aleksandrkrapivin19{random.randint(1000, 9999)}@ya.ru'

def generate_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_user():
    return {
        "username": "Тестовый Пользователь",
        "email": generate_email(),
        "password": generate_password()
    }