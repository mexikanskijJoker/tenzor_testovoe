import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config
from scenarios.base import BasePage


class DownloadPage(BasePage):
    """Страница загрузки СБИС"""

    def click_sbis_plugin(self):
        """Клик на 'СБИС Плагин'"""

        plugin_button = self.driver.find_element(
            By.CSS_SELECTOR, config.THIRD_SCENARIO["PLUGIN_BUTTON_SELECTOR"]
        )
        while True:
            plugin_button.click()
            elem = self.driver.find_element(
                By.XPATH,
                config.THIRD_SCENARIO["INSTALLER_LINK_XPATH"],
            ).text
            if not elem:
                pass
            else:
                break

    def click_download_file(self):
        """Клик на ссылку скачивание exe файла установщика"""

        download_button = self.driver.find_element(
            By.XPATH,
            config.THIRD_SCENARIO["INSTALLER_LINK_XPATH"],
        )
        download_button.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(
            lambda driver: any(
                filename.endswith(".exe")
                for filename in os.listdir(common.DOWNLOAD_FOLDER)
            )
        )

    def is_file_downloaded(self):
        """Скачан ли файл установщика"""

        is_exe_file_in_dir = [
            filename.endswith(".exe") for filename in os.listdir(common.DOWNLOAD_FOLDER)
        ]

        if len(is_exe_file_in_dir) != 0:
            return True

        return False

    def get_downloaded_file_size(self):
        """Возвращает размер файла в байтах"""

        file = os.listdir(common.DOWNLOAD_FOLDER)[0]
        file_size = os.path.getsize(common.DOWNLOAD_FOLDER + "/" + file)

        return round(file_size / 1048576, 2)


class MainPage(BasePage):
    """Главная страница https://sbis.ru/"""

    def download_sbis(self) -> DownloadPage:
        """Установка СБИС"""

        download_sbis_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    config.THIRD_SCENARIO["DOWNLOAD_SBIS_LINK_SELECTOR"],
                )
            )
        )
        self.driver.execute_script(
            config.THIRD_SCENARIO["CLICK_ACTION"], download_sbis_link
        )

        return DownloadPage(self.driver)
