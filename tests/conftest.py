import pytest
from selenium import webdriver

from utils.generators import generate_user


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    return generate_user()