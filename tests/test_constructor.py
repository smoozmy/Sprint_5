import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from src.data import BASE_URL
from src.locators import ConstructorLocators


class TestConstructor:

    @pytest.mark.parametrize('tab_locator, text', [
        (ConstructorLocators.TAB_SAUCE, 'Соусы'),
        (ConstructorLocators.TAB_TOPPING, 'Начинки'),
    ])
    def test_switch_sauce_topping(self, driver, tab_locator, text):
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(tab_locator)).click()

        current_tab_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(tab_locator)).text

        assert current_tab_text == text

    def test_switch_bread(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorLocators.TAB_TOPPING)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorLocators.TAB_BREAD)).click()

        current_tab_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorLocators.TAB_BREAD)).text

        assert current_tab_text == 'Булки'
