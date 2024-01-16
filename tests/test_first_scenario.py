from scenarios.first_scenario import MainPage


def test_first_scenario(browser):
    main_page = MainPage(browser)

    contacts_page = main_page.go_to_contacts()

    tensor_page = contacts_page.click_tensor_banner()
    contacts_page.switch_to_tensor_page()

    assert tensor_page.is_power_section_present() == True

    about_page = tensor_page.open_about_section()

    assert about_page

    assert about_page.is_work_section_present()

    assert about_page.are_photos_same_size() == True
