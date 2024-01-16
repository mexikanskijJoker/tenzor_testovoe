import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config


class BasePage:
    """Базовый класс страницы"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver


class AboutPage(BasePage):
    """Страница https://tensor.ru/about"""

    def are_photos_same_size(self) -> bool:
        """Проверка изображений на совпадение по размерам в блоке 'Работаем'"""
        try:
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

            is_photos_sizes_equal = all(
                photo == photos_size[0] for photo in photos_size
            )

            return is_photos_sizes_equal

        except Exception as e:
            logging.error(e)

    def is_work_section_present(self) -> bool:
        """Проверяет наличие блока 'Работаем' на странице"""
        try:
            work_section = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, config.FIRST_SCENARIO["WORK_BLOCK_XPATH"])
                )
            )

            return work_section.is_displayed()

        except Exception as e:
            logging.error(e)


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
            return power_section.is_displayed()

        except Exception as e:
            logging.error(e)

    def open_about_section(self) -> AboutPage:
        """Выполняет поиск ссылки на страницу '/about'"""
        try:
            about_section_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, config.FIRST_SCENARIO["ABOUT_BLOCK_SELECTOR"])
                )
            )

            about_section_button.click()

            return AboutPage(self.driver)

        except Exception as e:
            logging.error(e)


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

            return TensorPage(self.driver)

        except Exception as e:
            logging.error(e)

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

            return ContactsPage(self.driver)

        except Exception as e:
            logging.error(e)


# def run():
#     chromeOptions = Options()
#     chromeOptions.add_argument(common.DRIVER_OPTION)
#     driver = webdriver.Chrome(options=chromeOptions)
#     driver.get(common.SBIS_URL)

#     try:
#         main_page = MainPage(driver)
#         contacts_page = main_page.go_to_contacts()
#         tensor_page = contacts_page.click_tensor_banner()
#         contacts_page.switch_to_tensor_page()
#         print("Отображение блока силы", tensor_page.is_power_section_present())
#         about_page = tensor_page.open_about_section()
#         print("Отображение блока работы", about_page.is_work_section_present())
#         print(about_page.are_photos_same_size())
#     except Exception as e:
#         logging.error(e)

#     driver.quit()
