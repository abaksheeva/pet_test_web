from abc import ABC


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
