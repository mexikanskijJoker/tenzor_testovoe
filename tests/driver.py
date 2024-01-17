import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import configs.common as common


@pytest.fixture()
def browser():
    chromeOptions = Options()
    download_dir = (
        os.path.dirname(os.path.realpath(common.DOWNLOAD_FOLDER))
        + "/"
        + common.DOWNLOAD_FOLDER
    )
    chromeOptions.add_experimental_option(
        "prefs", {"download.default_directory": download_dir}
    )
    chromeOptions.add_argument(common.DRIVER_OPTION)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(common.SBIS_URL)
    yield driver
    driver.quit()
