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


"""def filter_test_cases():
    return [
        ('Filtering by name: 1 letter entered', 'x', [book[2]]),
        ('Filtering by first letters of the name', 'exp', [book[2]]),
        ('Filtering by letters in the middle of the name', 'for', [book[5], book[7]]),
        ('Filtering by last letters of the name''book', [book[7]]),
        ('Filtering by name: no filter results', 'gsdhsdthbsdfbdfabgs', [])
    ]"""
