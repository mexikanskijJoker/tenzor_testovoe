from scenarios.third_scenario import MainPage
import utils.utils as utils


def test_third_scenario(browser):
    """Тест для третьего сценария"""

    utils.create_or_remove_folder()

    main_page = MainPage(browser)

    download_page = main_page.download_sbis()

    download_page.click_sbis_plugin()

    download_page.click_download_file()

    # Проверка, скачался ли файл
    assert utils.is_file_downloaded()

    # Проверка на совпадение размера скачанного файла с указанными на сайте
    assert utils.get_downloaded_file_size() == download_page.get_expected_file_size()
