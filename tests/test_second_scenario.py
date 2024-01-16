from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import configs.common as common
from scenarios.second_scenario import MainPage


def test_second_scenario():
    chromeOptions = Options()
    chromeOptions.add_argument(common.DRIVER_OPTION)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(common.SBIS_URL)

    main_page = MainPage(driver)

    contacts_page = main_page.go_to_contacts()
    current_region = contacts_page.check_region_name()
    check_partners_list = contacts_page.is_partners_list_exist()
    current_partners_list = contacts_page.get_partners_list_text()

    assert current_region == "Свердловская обл."

    assert check_partners_list == True

    contacts_page.change_region()

    target_region = contacts_page.check_region_name()

    assert target_region == "Камчатский край"

    target_partners_list = contacts_page.get_partners_list_text()

    assert current_partners_list != target_partners_list

    target_url_and_title = contacts_page.check_url_and_title()

    assert target_url_and_title == (True, True)

    # Сформировать тест кейсы
