from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from src.generators import generate_user

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    return generate_user()