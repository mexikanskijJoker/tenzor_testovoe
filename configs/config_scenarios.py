FIRST_SCENARIO = {
    "ABOUT_BLOCK_SELECTOR": 'a[href="/about"]',
    "IMAGES_BLOCK_CLASSNAME": "tensor_ru-About__block3-image-wrapper",
    "PEOPLE_POWER_BLOCK_XPATH": '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div',
    "TENSOR_BLOCK_SELECTOR": 'a[href="https://tensor.ru/"]',
    "WORK_BLOCK_XPATH": '//*[@id="container"]/div[1]/div/div[4]',
}
"""Набор параметров для первого сценария"""

SECOND_SCENARIO = {
    "CURRENT_REGION_NAME": "Свердловская обл.",
    "PARTNERS_LIST_ELEMENT_XPATH": '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]',
    "REGION_ELEMENT_XPATH": '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span',
    "TARGET_REGION_ELEMENT_XPATH": '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span',
    "TARGET_TITLE_PART": "Камчатский край",
    "TARGET_URL_PART": "41-kamchatskij-kraj",
}
"""Набор параметров для второго сценария"""

THIRD_SCENARIO = {
    "BACKOFF_FACTOR": 1,
    "BYTES_IN_MB": 1048576,
    "CLICK_ACTION": "arguments[0].click();",
    "DOWNLOAD_SBIS_LINK_SELECTOR": 'a[href="/download?tab=ereport&innerTab=ereport25"]',
    "INSTALLER_LINK_XPATH": "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
    "PLUGIN_BUTTON_SELECTOR": 'div[data-id="plugin"]',
}
"""Набор параметров для третьего сценария"""
