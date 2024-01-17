from scenarios.first_scenario import MainPage


def test_first_scenario(browser):
    """Тест для первого сценария"""

    main_page = MainPage(browser)

    contacts_page = main_page.go_to_contacts()

    tensor_page = contacts_page.click_tensor_banner()
    contacts_page.switch_to_tensor_page()

    # Проверка отображения на странице блока 'Сила в людях'
    assert tensor_page.is_power_section_present()

    about_page = tensor_page.open_about_section()

    # Проверка открытия страницы 'Подробнее'
    assert about_page

    # Провека отображения блока 'Работаем'
    assert about_page.is_work_section_present()

    # Проверка на совпадение всех изображений блока 'Работаем' по размерам
    assert about_page.are_photos_same_size()
