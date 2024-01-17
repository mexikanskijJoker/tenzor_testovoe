import os

CONTACTS = "Контакты"
"""Контакты"""

DOWNLOAD_FOLDER = "tenzor_downloads"
"""Папка для загрузки установщика"""

SBIS_URL = "https://sbis.ru/"
"""URL-адрес СБИС"""

FULL_DOWNLOAD_PATH = os.path.join(
    os.path.dirname(os.path.realpath(DOWNLOAD_FOLDER)),
    DOWNLOAD_FOLDER,
)
"""Полный путь к папке для установки плагина"""

EXP_OPTIONS = {
    "download.default_directory": FULL_DOWNLOAD_PATH,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
"""Набор экспериментальных опций"""

CHROME_OPTIONS = ("prefs", {**EXP_OPTIONS})
"""Опции для браузера Chrome"""
