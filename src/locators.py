from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_EMAIL_INPUT = By.XPATH, '//input[@name="name"]'               # Поле ввода почты
    LOGIN_PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'          # Поле ввода пароля
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'                 # Кнопка 'Войти'
    LOGIN_TITLE = By.XPATH, '//h2[text()="Вход"]'                       # Заголовок страницы

class RegistrationLocators:
    REGISTER_NAME_INPUT = By.XPATH, '(//input[@name="name"])[1]'        # Поле ввода имени
    REGISTER_EMAIL_INPUT = By.XPATH, '(//input[@name="name"])[2]'       # Поле ввода почты
    REGISTER_PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'       # Поле ввода пароля
    REGISTER_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]' # Кнопка 'Зарегистрироваться'
    ERROR_MESSAGE = By.XPATH, '//p[text()="Некорректный пароль"]'       # Текст ошибки 'Некорректный пароль'
    LOGIN_PAGE_BUTTON = By.XPATH, '//a[contains(@class, "Auth_link")]'  # Кнопка перехода к экрану авторизации
    REGISTRATION_TITLE = By.XPATH, '//h2[text()="Регистрация"]'         # Заголовок страницы

class ConstructorLocators:
    LOGIN_PAGE_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'  # Кнопка перехода к экрану авторизации
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'        # Кнопка 'Оформить заказ'
    LOGO_STELLAR_BURGER = By.XPATH, '//div[contains(@class, "logo")]'   # Лого
    TAB_CURRENT = By.XPATH, '//div[contains(@class, "tab_type_current")]' # Активная вкладка
    TAB_BREAD = By.XPATH, '//span[contains(text(), "Булки")]/..'        # Вкладка 'Булки'
    TAB_SAUCE = By.XPATH, '//span[contains(text(), "Соусы")]/..'        # Вкладка 'Соусы'
    TAB_TOPPING = By.XPATH, '//span[contains(text(), "Начинки")]/..'    # Вкладка 'Начинки'

class ForgotPasswordLocators:
    LOGIN_PAGE_BUTTON = By.XPATH, '//a[text()="Войти"]'                 # Кнопка перехода к экрану авторизации

class ProfileLocators:
    PROFILE_TAB_LABEL = By.XPATH, '//a[text()="Профиль"]'               # Вкладка 'Профиль' в личном кабинете
    LOGOUT_TAB_BUTTON = By.XPATH, '//button[text()="Выход"]'            # Кнопка выхода из личного кабинета
    PROFILE_PAGE_BUTTON = By.XPATH, '//a[@href="/account"]'             # Кнопка перехода к экрану профиля