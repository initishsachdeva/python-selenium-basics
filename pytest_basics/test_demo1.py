# pytest test method should be start with name test
import pytest


def test_firstProgram():
    print('hello')


# to group test under some tags like Smoke or Sanity , we have give below expression
@pytest.mark.smoke
@pytest.mark.skip
def test_secondProgram():
    print('second test function')


@pytest.mark.xfail
def test_thirdProgram():
    print('third test function')
