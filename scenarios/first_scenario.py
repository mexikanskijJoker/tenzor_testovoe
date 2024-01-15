import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs.common import CONTACTS, SBIS_URL
from configs.config_first_scenario import (
    ABOUT_BLOCK_SELECTOR,
    DRIVER_OPTION,
    IMAGES_BLOCK_CLASSNAME,
    PEOPLE_POWER_BLOCK_XPATH,
    TENSOR_BLOCK_SELECTOR,
    WORK_BLOCK_XPATH,
)
from configs.logging import FIRST_SCENARIO_OUTPUT_FILENAME, LOG_LEVEL


class AboutPage:
    """Страница https://tensor.ru/about"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Проверяет, все ли изображения блока 'Работаем' обладают одинаковыми размерами
    def are_photos_same_size(self) -> bool:
        photos = self.driver.find_elements(
            By.CLASS_NAME,
            IMAGES_BLOCK_CLASSNAME,
        )
        first_photo_size = photos[0].size
        for photo in photos[1:]:
            if photo.size != first_photo_size:
                return False

        return True

    # Проверяет наличие блока 'Работаем'
    def is_work_section_present(self) -> bool:
        work_section = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, WORK_BLOCK_XPATH))
        )

        return work_section.is_displayed()


class TensorPage:
    """Страница https://tensor.ru/"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Проверяет наличие блока 'Сила в людях'
    def is_power_section_present(self) -> bool:
        power_section = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    PEOPLE_POWER_BLOCK_XPATH,
                )
            )
        )
        # StaleElementReferenceException обработать
        return power_section.is_displayed()

    # Выполняет поиск ссылки на страницу '/about'
    def open_about_section(self) -> AboutPage:
        about_section_button = self.driver.find_element(
            By.CSS_SELECTOR, ABOUT_BLOCK_SELECTOR
        )
        about_section_button.click()

        return AboutPage(self.driver)


class ContactsPage:
    """Страница 'Контакты'"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Выполняет поиск баннера 'Тензора' и, кликая на него, возвращает страницу https://tensor.ru/
    def click_tensor_banner(self) -> TensorPage:
        tensor_banner = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, TENSOR_BLOCK_SELECTOR))
        )
        tensor_banner.click()

        return TensorPage(self.driver)

    # Открывает страницу https://tensor.ru/ в новом окне
    def switch_to_tensor_page(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[1])


class MainPage:
    """Стартовая страница https://sbis.ru/"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Возвращает страницу Контакты
    def go_to_contacts(self) -> ContactsPage:
        contacts_link = self.driver.find_element(By.LINK_TEXT, CONTACTS)
        contacts_link.click()

        return ContactsPage(self.driver)


def run_first_scenario():
    logging.basicConfig(
        level=LOG_LEVEL,
        filename=FIRST_SCENARIO_OUTPUT_FILENAME,
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    chromeOptions = Options()
    chromeOptions.add_argument(DRIVER_OPTION)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(SBIS_URL)

    main_page = MainPage(driver)
    contacts_page = main_page.go_to_contacts()
    tensor_page = contacts_page.click_tensor_banner()
    contacts_page.switch_to_tensor_page()
    print("Отображение блока силы", tensor_page.is_power_section_present())
    about_page = tensor_page.open_about_section()
    print("Отображение блока работы", about_page.is_work_section_present())
    print("Размеры фоток" + str(about_page.are_photos_same_size()) + "\n")

    driver.quit()
