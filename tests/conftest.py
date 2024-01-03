import allure
import pytest
from selenium import webdriver

from data import urls


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    output = yield
    report = output.get_result()

    if report.failed:
        if 'browser' not in item.fixturenames:
            print('Fail to take screenshot')
            return

        driver = item.funcargs['browser']
        allure.attach(
            driver.get_screenshot_as_png(),
            name=report.nodeid,
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()
