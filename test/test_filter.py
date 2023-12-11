import pytest

from data.test_data import books
from page_objects.main_page import MainPage


def test_no_filter_shows_all_books(browser):
    """Verify all books present if no filter applied"""
    page = MainPage(browser)
    page.verify_visible_books_are(books)


@pytest.mark.parametrize("text, expected_books, test_case_name",
                         [
                             ('x', [books[2]], 'Filtering by name: 1 letter entered'),
                             ('exp', [books[2]], 'Filtering by first letters of the name'),
                             ('for', [books[5], books[7]], 'Filtering by letters in the middle of the name'),
                             ('book', [books[7]], 'Filtering by last letters of the name'),
                             ('gsdhsdthbsdfbdfabgs', [], 'Filtering by name: no filter results'),
                         ]
                         )
def test_single_result(browser, text, expected_books, test_case_name):
    """Verify filter functionality"""
    page = MainPage(browser)
    page.enter_text(text)
    page.verify_count_of_books(len(expected_books))
    page.verify_visible_books_are(expected_books)
