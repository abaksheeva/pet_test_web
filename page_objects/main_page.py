from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class MainPage(BasePage):

    INPUT_ID = "searchBar"
    BOOKS = "//li[not (contains(@class, 'ui-screen-hidden'))]"
    CLEAR_BTN = "ui-input-clear"

    def enter_text(self, text):
        input_field = self.driver.find_element(By.ID, self.INPUT_ID)
        input_field.send_keys(text)

    def get_number_of_books(self):
        return len(self.driver.find_elements(By.XPATH, self.BOOKS))

    def get_visible_books(self):
        books_elems = self.driver.find_elements(By.XPATH, self.BOOKS)
        return [book_elem.text.split('\n') for book_elem in books_elems]

    def verify_count_of_books(self, expected_cnt):
        print(f"Expected {expected_cnt} books")
        WebDriverWait(self.driver, 5).until(lambda x: self.get_number_of_books() == expected_cnt)

    def verify_visible_books_are(self, expected_books):
        print(f"Expected books: {str(expected_books)}")
        text = self.get_visible_books()
        print(f"Actual books: {text}")
        return expected_books == text

    def click_clear_button(self):
        self.driver.find_element(By.CLASS_NAME, self.CLEAR_BTN)

    def verify_clear_button_existence(self, should_exist=True):
        if should_exist:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.CLEAR_BTN))
        else:
            WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located(self.CLEAR_BTN))
