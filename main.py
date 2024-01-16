import logging

from configs.logging import FIRST_SCENARIO_OUTPUT_FILENAME, LOG_LEVEL
from tests.test_second_scenario import test_second_scenario


def main():
    logging.basicConfig(
        level=LOG_LEVEL,
        filename=FIRST_SCENARIO_OUTPUT_FILENAME,
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    test_second_scenario()


if __name__ == "__main__":
    main()
