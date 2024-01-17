import configs.config_scenarios as config
from scenarios.second_scenario import MainPage


def test_second_scenario(browser):
    """Тест для второго сценария"""

    main_page = MainPage(browser)

    contacts_page = main_page.go_to_contacts()
    default_region = contacts_page.check_region_name()
    check_partners_list = contacts_page.is_partners_list_exist()
    default_partners_list = contacts_page.get_partners_list_text()

    # Проверка отображения Свердловской обл. в качестве выбранного региона по умолчанию
    assert default_region == config.SECOND_SCENARIO["DEFAULT_REGION_NAME"]

    # Проверка отображения списка партнёров
    assert check_partners_list

    contacts_page.change_region()

    target_region = contacts_page.check_region_name()

    # Проверка отображения Камчатского края как выбранного после смены региона
    assert target_region == config.SECOND_SCENARIO["TARGET_TITLE_PART"]

    target_partners_list = contacts_page.get_partners_list_text()

    # Проверка изменения списка партнёров до и после смены региона
    assert default_partners_list != target_partners_list

    target_url_and_title = contacts_page.check_url_and_title()

    # Проверка содержания в URL-адрес и тайтле сайта информации о выбранном регионе
    assert target_url_and_title == (True, True)
