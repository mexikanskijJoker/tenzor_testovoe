import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import configs.common as common


@pytest.fixture()
def browser():
    chromeOptions = Options()
    chromeOptions.add_experimental_option(*common.CHROME_OPTIONS)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(common.SBIS_URL)
    yield driver
    driver.quit()
