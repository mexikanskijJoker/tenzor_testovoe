import logging
import os
import shutil

import configs.common as common
import configs.config_scenarios as config


def create_folder() -> None:
    """Создаёт папку для загрузки плагина"""

    return os.mkdir(common.DOWNLOAD_FOLDER)


def create_or_remove_folder() -> None:
    """Создаёт папку для загрузки плагина или удаляет её в зависимости от того, существует ли уже такая папка в корне проекта"""

    root_path = os.getcwd()

    folder_path = os.path.join(root_path, common.DOWNLOAD_FOLDER)

    if os.path.isdir(folder_path):
        # Происходит удаление папки с установщиком
        remove_folder()

    # Происходит создание папки для загрузки установщика
    create_folder()

    return


def get_downloaded_file_size() -> float:
    """Возвращает размер скачанного установщика в МБ"""

    try:
        file = os.listdir(common.DOWNLOAD_FOLDER)[0]
        full_exe_file_path = os.path.join(
            os.path.dirname(
                os.path.join(
                    os.path.realpath(common.DOWNLOAD_FOLDER), common.DOWNLOAD_FOLDER
                )
            ),
            file,
        )
        file_size = os.path.getsize(full_exe_file_path)

    except Exception as e:
        logging.error(e)

    downloaded_file_size = round(file_size / config.THIRD_SCENARIO["BYTES_IN_MB"], 2)

    return downloaded_file_size


def is_file_downloaded() -> bool:
    """Скачан ли файл установщика"""

    try:
        is_exe_file_in_dir = [
            filename.endswith(".exe") for filename in os.listdir(common.DOWNLOAD_FOLDER)
        ]
    except Exception as e:
        logging.error(e)

    if len(is_exe_file_in_dir) != 0:
        return True

    return False


def remove_folder() -> None:
    """Удаление папки для загрузки плагина"""

    return shutil.rmtree(common.DOWNLOAD_FOLDER)
