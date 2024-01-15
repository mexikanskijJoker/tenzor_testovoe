import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs.common import CONTACTS, SBIS_URL
from configs.config_first_scenario import DRIVER_OPTION
from configs.config_second_scenario import (
    PARTNERS_LIST_ELEMENT_XPATH,
    REGION_ELEMENT_XPATH,
    TARGET_REGION_ELEMENT_XPATH,
    TARGET_TITLE_PART,
    TARGET_URL_PART,
)
from configs.logging import LOG_LEVEL, SECOND_SCENARIO_OUTPUT_FILENAME


class ContactsPage:
    """Страница 'Контакты'"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Функция осуществляет обновление инфы на сайте с учётом заданного региона
    def change_region(self) -> None:
        region_name = self.get_current_region()
        region_name.click()
        target_region = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, TARGET_REGION_ELEMENT_XPATH))
        )
        target_region.click()
        time.sleep(1)

    # Функция возвращает название текущего региона
    def check_region_name(self) -> str:
        region_name = self.get_current_region()
        return region_name.text

    # Функция проверяет url-адрес и title сайта на наличие инфы об указанном регионе
    def check_url_and_title(self) -> tuple[bool, bool]:
        current_url = self.driver.current_url
        current_title = self.driver.title
        is_url_correct = TARGET_URL_PART in current_url
        is_title_correct = TARGET_TITLE_PART in current_title

        return is_url_correct, is_title_correct

    # Функция возвращает элемент, содержащий выбранный регион(по умолчанию текущий, 66)
    def get_current_region(self) -> WebElement:
        region = self.driver.find_element(By.XPATH, REGION_ELEMENT_XPATH)

        return region

    # Функция возвращает элемент, содержащий инфу о партнёрах
    def get_partners_list(self) -> WebElement:
        partners_list = self.driver.find_element(By.XPATH, PARTNERS_LIST_ELEMENT_XPATH)

        return partners_list

    # Функция возвращает содержание элемента о партнёрах
    def get_partners_list_text(self) -> str:
        partners_list = self.get_partners_list()
        return partners_list.text

    # Функция возвращает True, в случае если на странице отображается инфа о партнёрах
    def is_partners_list_exist(self) -> bool:
        partners_list = self.get_partners_list()

        return partners_list.is_displayed()


class MainPage:
    """Стартовая страница https://sbis.ru/"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Возвращает страницу Контакты
    def go_to_contacts(self) -> ContactsPage:
        contacts_link = self.driver.find_element(By.LINK_TEXT, CONTACTS)
        contacts_link.click()

        return ContactsPage(self.driver)


def run_second_scenario():
    logging.basicConfig(
        level=LOG_LEVEL,
        filename=SECOND_SCENARIO_OUTPUT_FILENAME,
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    chromeOptions = Options()
    chromeOptions.add_argument(DRIVER_OPTION)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(SBIS_URL)

    main_page = MainPage(driver)
    contacts_page = main_page.go_to_contacts()
    print("Название региона", contacts_page.check_region_name())
    print("Список партнёров", contacts_page.is_partners_list_exist())
    contacts_page.get_partners_list_text()
    contacts_page.change_region()
    print("Название региона", contacts_page.check_region_name())
    print("Урл и тайтл", contacts_page.check_url_and_title())

    driver.quit()
