import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config
from scenarios.base import BasePage


class AboutPage(BasePage):
    """Страница https://tensor.ru/about"""

    def are_photos_same_size(self) -> bool:
        """Проверка изображений на совпадение по размерам в блоке 'Работаем'"""

        photos = (
            WebDriverWait(self.driver, 5)
            .until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, config.FIRST_SCENARIO["IMAGES_BLOCK_CLASSNAME"])
                )
            )
            .find_elements(
                By.CLASS_NAME, config.FIRST_SCENARIO["IMAGES_BLOCK_CLASSNAME"]
            )
        )

        photos_size = list(map(lambda photo: photo.size, photos))

        return all(photo == photos_size[0] for photo in photos_size)

    def is_work_section_present(self) -> bool:
        """Проверяет наличие блока 'Работаем' на странице"""
        try:
            work_section = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, config.FIRST_SCENARIO["WORK_BLOCK_XPATH"])
                )
            )

        except Exception as e:
            logging.error(e)

        return work_section.is_displayed()


class TensorPage(BasePage):
    """Страница https://tensor.ru/"""

    def is_power_section_present(self) -> bool:
        """Проверяет наличие блока 'Сила в людях' на странице"""
        try:
            power_section = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        config.FIRST_SCENARIO["PEOPLE_POWER_BLOCK_XPATH"],
                    )
                )
            )

        except Exception as e:
            logging.error(e)

        return power_section.is_displayed()

    def open_about_section(self) -> AboutPage:
        """Выполняет поиск ссылки на страницу '/about'"""
        try:
            about_section_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, config.FIRST_SCENARIO["ABOUT_BLOCK_SELECTOR"])
                )
            )

            about_section_button.click()

        except Exception as e:
            logging.error(e)

        return AboutPage(self.driver)


class ContactsPage(BasePage):
    """Страница 'Контакты'"""

    def click_tensor_banner(self) -> TensorPage:
        """Выполняет поиск баннера 'Тензора' и, кликая на него, возвращает страницу https://tensor.ru/"""
        try:
            tensor_banner = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, config.FIRST_SCENARIO["TENSOR_BLOCK_SELECTOR"])
                )
            )

            tensor_banner.click()

        except Exception as e:
            logging.error(e)

        return TensorPage(self.driver)

    def switch_to_tensor_page(self) -> None:
        """Открывает страницу https://tensor.ru/ в новом окне"""
        self.driver.switch_to.window(self.driver.window_handles[1])


class MainPage(BasePage):
    """Стартовая страница https://sbis.ru/"""

    def go_to_contacts(self) -> ContactsPage:
        """Возвращает страницу Контакты"""
        try:
            contacts_link = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, common.CONTACTS))
            )

            contacts_link.click()

        except Exception as e:
            logging.error(e)

        return ContactsPage(self.driver)
