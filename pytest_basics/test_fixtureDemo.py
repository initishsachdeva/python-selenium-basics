import pytest


# in python fixtures are just like the junit and testng frameworks test.before and test.after methods. In pytest for
# before method execution we define like below and for after test execution we have keyword "yield" to perform post
# test execution operations


@pytest.fixture()
def setup1():
    print("I will be executed first")
    yield
    print("I will execute last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo")
