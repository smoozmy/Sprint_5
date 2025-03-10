from conftest import driver



class TestLogin:
    def test_login_from_login_page(self, driver):
        pass
        # page = LoginPage(driver)
        # page.open()
        # page.login(TEST_USER["email"], TEST_USER["password"])
        #
        # page.wait_for_url(BASE_URL)
        #
        # assert driver.current_url == BASE_URL

    def test_login_from_registration_page(self, driver):
        pass
        # register_page = RegistrationPage(driver)
        # register_page.open()
        # register_page.go_to_login_page()
        #
        # login_page = LoginPage(driver)
        # login_page.login(TEST_USER["email"], TEST_USER["password"])
        # login_page.wait_for_url(BASE_URL)
        #
        # assert driver.current_url == BASE_URL


    def test_login_from_constructor_page(self, driver):
        pass
        # constructor_page = ConstructorPage(driver)
        # constructor_page.open()
        # constructor_page.go_to_login_page()
        #
        # login_page = LoginPage(driver)
        # login_page.login(TEST_USER["email"], TEST_USER["password"])
        # sleep(5)
        # login_page.wait_for_url(BASE_URL)
        #
        # assert driver.current_url == BASE_URL

    def test_login_from_forgot_page(self, driver):
        pass

    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # class BasePage:
    #     def __init__(self, driver):
    #         self.driver = driver
    #
    #     def click(self, locator):
    #         WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()
    #
    #     def enter_text(self, locator, text):
    #         WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)
    #
    #     def get_element(self, locator):
    #         return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
    #
    #     def wait_for_url(self, url):
    #         WebDriverWait(self.driver, 5).until(EC.url_to_be(url))