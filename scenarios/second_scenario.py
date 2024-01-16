import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config


class BasePage:
    """Базовый класс страницы"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver


class ContactsPage(BasePage):
    """Страница 'Контакты'"""

    def change_region(self) -> None:
        """Смена региона"""
        try:
            region_name = self.get_current_region()
            region_name.click()
            target_region = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        config.SECOND_SCENARIO["TARGET_REGION_ELEMENT_XPATH"],
                    )
                )
            )
            target_region.click()
            time.sleep(1)

        except Exception as e:
            logging.error(e)

    def check_region_name(self) -> str:
        """Возвращает название текущего региона"""
        try:
            region_name = self.get_current_region()

            return region_name.text

        except Exception as e:
            logging.error(e)

    def check_url_and_title(self) -> tuple[bool, bool]:
        """Проверка url-адрес и title сайта на наличие инфы об указанном регионе"""
        try:
            current_url = self.driver.current_url
            current_title = self.driver.title
            is_url_correct = config.SECOND_SCENARIO["TARGET_URL_PART"] in current_url
            is_title_correct = (
                config.SECOND_SCENARIO["TARGET_TITLE_PART"] in current_title
            )

            return is_url_correct, is_title_correct

        except Exception as e:
            logging.error(e)

    def get_current_region(self) -> WebElement:
        """Возвращает элемент, содержащий выбранный регион(по умолчанию текущий, 66)"""
        try:
            region = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, config.SECOND_SCENARIO["REGION_ELEMENT_XPATH"])
                )
            )

            return region

        except Exception as e:
            logging.error(e)

    def get_partners_list(self) -> WebElement:
        """Возвращает элемент, содержащий инфу о партнёрах"""
        try:
            partners_list = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, config.SECOND_SCENARIO["PARTNERS_LIST_ELEMENT_XPATH"])
                )
            )

            return partners_list

        except Exception as e:
            logging.error(e)

    def get_partners_list_text(self) -> str:
        """Возвращает содержание элемента о партнёрах"""
        try:
            partners_list = self.get_partners_list()

            return partners_list.text

        except Exception as e:
            logging.error(e)

    def is_partners_list_exist(self) -> bool:
        """Возвращает True, в случае если на странице отображается инфа о партнёрах"""
        try:
            partners_list = self.get_partners_list()

            return partners_list.is_displayed()

        except Exception as e:
            logging.error(e)


class MainPage(BasePage):
    """Стартовая страница https://sbis.ru/"""

    def go_to_contacts(self) -> ContactsPage:
        """Возвращает страницу Контакты"""
        try:
            contacts_link = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, common.CONTACTS))
            )
            contacts_link.click()

            return ContactsPage(self.driver)

        except Exception as e:
            logging.error(e)


# def run():
#     chromeOptions = Options()
#     chromeOptions.add_argument(common.DRIVER_OPTION)
#     driver = webdriver.Chrome(options=chromeOptions)
#     driver.get(common.SBIS_URL)

#     main_page = MainPage(driver)
#     contacts_page = main_page.go_to_contacts()
#     print("Название региона", contacts_page.check_region_name())
#     print("Список партнёров", contacts_page.is_partners_list_exist())
#     contacts_page.get_partners_list_text()
#     contacts_page.change_region()
#     print("Название региона", contacts_page.check_region_name())
#     print("Урл и тайтл", contacts_page.check_url_and_title())

#     driver.quit()
