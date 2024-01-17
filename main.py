from tests.driver import browser

from tests.test_first_scenario import test_first_scenario
from tests.test_second_scenario import test_second_scenario
from tests.test_third_scenario import test_third_scenario


def main():
    test_first_scenario(browser())
    test_second_scenario(browser())
    test_third_scenario(browser())


if __name__ == "__main__":
    main()
