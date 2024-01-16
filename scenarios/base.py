from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Базовый класс страницы"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
