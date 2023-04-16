import pytest


# in python fixtures are just like the junit and testng frameworks test.before and test.after methods. In pytest for
# before method execution we define like below and for after test execution we have keyword "yield" to perform post
# test execution operations

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["abc", "def", "abcdef.com"]


@pytest.fixture(params=[("chrome", "ABC", "DEF"), ("Firefox", "IJK"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
