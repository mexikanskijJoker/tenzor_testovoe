import configs.config_scenarios as config
from scenarios.second_scenario import MainPage


def test_second_scenario(browser):
    main_page = MainPage(browser)

    contacts_page = main_page.go_to_contacts()
    current_region = contacts_page.check_region_name()
    check_partners_list = contacts_page.is_partners_list_exist()
    current_partners_list = contacts_page.get_partners_list_text()

    assert current_region == config.SECOND_SCENARIO["CURRENT_REGION_NAME"]

    assert check_partners_list == True

    contacts_page.change_region()

    target_region = contacts_page.check_region_name()

    assert target_region == config.SECOND_SCENARIO["TARGET_TITLE_PART"]

    target_partners_list = contacts_page.get_partners_list_text()

    assert current_partners_list != target_partners_list

    target_url_and_title = contacts_page.check_url_and_title()

    assert target_url_and_title == (True, True)
