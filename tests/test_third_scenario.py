from scenarios.third_scenario import MainPage


def test_third_scenario(browser):
    """Тест для третьего сценария"""

    main_page = MainPage(browser)

    download_page = main_page.download_sbis()

    download_page.click_sbis_plugin()

    download_page.click_download_file()

    # Проверка, скачался ли файл
    assert download_page.is_file_downloaded()

    # Проверка на совпадение размеров скачанного файла с указанными на сайте
    assert download_page.get_downloaded_file_size() == 7.02
