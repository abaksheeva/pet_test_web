import allure
import pytest

from data.test_data import books, testcases
from pages.main_page import MainPage


@allure.title("Verify all books present if no filter applied")
def test_no_filter_shows_all_books(browser):
    page = MainPage(browser)
    page.verify_visible_books_are([value for value in books.values()])


@allure.title("Verify filter functionality")
@pytest.mark.parametrize("testcase", testcases.values(), ids=testcases.keys())
def test_filter(browser, testcase):
    page = MainPage(browser)
    page.enter_text(testcase[0])
    page.verify_count_of_books(len(testcase[1]))
    page.verify_visible_books_are(testcase[1])


@allure.title("Verify filter is cleared after clicking x button")
def test_filter_cleared_by_x_button(browser):
    page = MainPage(browser)
    book_name = books.get(1)[0]
    page.enter_text(book_name)
    page.verify_count_of_books(1)

    page.click_clear_button()
    page.verify_count_of_books(len(books))
