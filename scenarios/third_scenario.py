import logging
import os
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
import configs.config_scenarios as config
from scenarios.base import BasePage


class DownloadPage(BasePage):
    """Страница загрузки СБИС"""

    def click_sbis_plugin(self) -> None:
        """Клик на 'СБИС Плагин'"""

        try:
            plugin_button = self.driver.find_element(
                By.CSS_SELECTOR, config.THIRD_SCENARIO["PLUGIN_BUTTON_SELECTOR"]
            )
            for i in range(1, 10):
                plugin_button.click()
                elem = self.driver.find_element(
                    By.XPATH,
                    config.THIRD_SCENARIO["INSTALLER_LINK_XPATH"],
                ).text
                if not elem:
                    time.sleep(config.THIRD_SCENARIO["BACKOFF_FACTOR"] * (2 ** (i - 1)))
                else:
                    break

        except Exception as e:
            logging.error(e)

        return

    def click_download_file(self) -> None:
        """Клик на ссылку скачивание exe файла установщика"""

        try:
            download_button = self.driver.find_element(
                By.XPATH,
                config.THIRD_SCENARIO["INSTALLER_LINK_XPATH"],
            )
            download_button.click()

            wait = WebDriverWait(self.driver, common.DEFAULT_TIMEOUT)
            wait.until(
                lambda driver: any(
                    filename.endswith(".exe")
                    for filename in os.listdir(common.DOWNLOAD_FOLDER)
                )
            )

        except Exception as e:
            logging.error(e)

        return

    def get_expected_file_size(self) -> float:
        """Возвращает ожидаемый размер установщика в МБ"""

        try:
            installer_elem = self.driver.find_element(
                By.XPATH,
                config.THIRD_SCENARIO["INSTALLER_LINK_XPATH"],
            ).text

        except Exception as e:
            logging.error(e)

        file_size = float(re.findall(r"\d+.\d+", installer_elem)[0])

        return file_size


class MainPage(BasePage):
    """Главная страница https://sbis.ru/"""

    def download_sbis(self) -> DownloadPage:
        """Установка СБИС"""

        try:
            download_sbis_link = WebDriverWait(
                self.driver, common.DEFAULT_TIMEOUT
            ).until(
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

        except Exception as e:
            logging.error(e)

        return DownloadPage(self.driver)
