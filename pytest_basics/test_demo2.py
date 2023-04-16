import pytest


def test_function1():
    msg = "hello"
    assert msg == "Hi, lets get a failed test"


@pytest.mark.smoke
def test_function2():
    a = 2
    b = 6
    assert a + 4 == b, "addition of two numbers"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
