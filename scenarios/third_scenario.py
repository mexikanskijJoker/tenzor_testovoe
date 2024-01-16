import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import configs.common as common
from scenarios.base import BasePage


class DownloadPage(BasePage):
    """Страница загрузки СБИС"""

    def click_sbis_plugin(self):
        plugin_button = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-id="plugin"]'
        )
        while True:
            plugin_button.click()
            elem = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
            ).text
            if not elem:
                pass
            else:
                break

    def click_download_file(self):
        download_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
        )
        download_button.click()

        time.sleep(5)


class MainPage(BasePage):
    """Главная страница https://sbis.ru/"""

    def download_sbis(self) -> DownloadPage:
        """Установка СБИС"""

        download_sbis_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'a[href="/download?tab=ereport&innerTab=ereport25"]',
                )
            )
        )
        self.driver.execute_script("arguments[0].click();", download_sbis_link)

        return DownloadPage(self.driver)


def run():
    chromeOptions = Options()
    download_dir = (
        os.path.dirname(os.path.realpath("tenzor_downloads")) + "/tenzor_downloads"
    )
    chromeOptions.add_experimental_option(
        "prefs", {"download.default_directory": download_dir}
    )
    chromeOptions.add_argument(common.DRIVER_OPTION)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(common.SBIS_URL)
    main_page = MainPage(driver)

    download_page = main_page.download_sbis()
    download_page.click_sbis_plugin()
    download_page.click_download_file()


if __name__ == "__main__":
    run()
