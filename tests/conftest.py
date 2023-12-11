import pytest
from selenium import webdriver

from data import urls


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()
