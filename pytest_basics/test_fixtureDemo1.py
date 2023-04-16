import pytest
from selenium.webdriver.common.by import By

from pytest_basics.BaseClass import BaseClass


# if you want to use same fixture for different functions then you define such in Class levels rather than mentioning
# again and again in function parameters. Just add the scope to the class level in conftest.py file

@pytest.mark.usefixtures("setup")
class TestExample:
    landingPageTitle = (By.XPATH, "//*[@class='title']")

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")

    def landingPage(self):
        title = self.driver.find_element(*TestExample.landingPageTitle).text
        return title
