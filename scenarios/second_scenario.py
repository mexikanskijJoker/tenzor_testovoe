import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config
from scenarios.base import BasePage


class ContactsPage(BasePage):
    """Страница 'Контакты'"""

    def change_region(self) -> None:
        """Смена региона"""
        try:
            region_name = self.get_current_region()
            region_name.click()
            target_region = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        config.SECOND_SCENARIO["TARGET_REGION_ELEMENT_XPATH"],
                    )
                )
            )
            target_region.click()
            time.sleep(config.THIRD_SCENARIO["BACKOFF_FACTOR"])

        except Exception as e:
            logging.error(e)

    def check_region_name(self) -> str:
        """Возвращает название текущего региона"""
        try:
            region_name = self.get_current_region()

        except Exception as e:
            logging.error(e)

        return region_name.text

    def check_url_and_title(self) -> tuple[bool, bool]:
        """Проверка url-адрес и title сайта на наличие инфы об указанном регионе"""
        try:
            current_url = self.driver.current_url
            current_title = self.driver.title
            is_url_correct = config.SECOND_SCENARIO["TARGET_URL_PART"] in current_url
            is_title_correct = (
                config.SECOND_SCENARIO["TARGET_TITLE_PART"] in current_title
            )

        except Exception as e:
            logging.error(e)

        return is_url_correct, is_title_correct

    def get_current_region(self) -> WebElement:
        """Возвращает элемент, содержащий выбранный регион(по умолчанию текущий, 66)"""
        try:
            region = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, config.SECOND_SCENARIO["REGION_ELEMENT_XPATH"])
                )
            )

        except Exception as e:
            logging.error(e)

        return region

    def get_partners_list(self) -> WebElement:
        """Возвращает элемент, содержащий инфу о партнёрах"""
        try:
            partners_list = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, config.SECOND_SCENARIO["PARTNERS_LIST_ELEMENT_XPATH"])
                )
            )

        except Exception as e:
            logging.error(e)

        return partners_list

    def get_partners_list_text(self) -> str:
        """Возвращает содержание элемента о партнёрах"""
        try:
            partners_list = self.get_partners_list()

        except Exception as e:
            logging.error(e)

        return partners_list.text

    def is_partners_list_exist(self) -> bool:
        """Возвращает True, в случае если на странице отображается инфа о партнёрах"""
        try:
            partners_list = self.get_partners_list()

        except Exception as e:
            logging.error(e)

        return partners_list.is_displayed()


class MainPage(BasePage):
    """Стартовая страница https://sbis.ru/"""

    def go_to_contacts(self) -> ContactsPage:
        """Возвращает страницу Контакты"""
        try:
            contacts_link = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.LINK_TEXT, common.CONTACTS))
            )
            contacts_link.click()

        except Exception as e:
            logging.error(e)

        return ContactsPage(self.driver)
