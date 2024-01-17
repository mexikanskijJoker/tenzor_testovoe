import logging
import os

import configs.common as common
import configs.config_scenarios as config


def get_downloaded_file_size() -> float:
    """Возвращает размер файла в байтах"""

    try:
        file = os.listdir(common.DOWNLOAD_FOLDER)[0]
        file_size = os.path.getsize(common.DOWNLOAD_FOLDER + "/" + file)
    except Exception as e:
        logging.error(e)

    return round(file_size / config.THIRD_SCENARIO["BYTES_IN_MB"], 2)


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
