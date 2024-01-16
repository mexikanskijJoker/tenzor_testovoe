# from tests.driver import browser
# from tests.test_first_scenario import test_first_scenario
# from tests.test_second_scenario import test_second_scenario
# from test.test_third_scenario import test_third_scenario


from scenarios.third_scenario import run


def main():
    # test_first_scenario(browser())
    # test_second_scenario(browser())
    run()


if __name__ == "__main__":
    main()
