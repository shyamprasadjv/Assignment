import pytest
import pytest_dependency
from test_case.question2 import searchbar,utilites
@pytest.mark.skipif("Atcost.in | Your money buys a LOT MORE ... With Us"=="title",reason="if the title is equal the skip the test script")
utilites()
searchbar()

@pytest.mark.depedency
def test_login():
    print('in test depedency')
@pytest.mark.dependecy(depends=["test_login"])    """ if test_login fails the test_logout method will not execute"""
def test_logout():
    print('in logout method')


pytestmark=pytest.mark.skip(reason="skip the moudule")#If user want to the skip the entire module you can use this pytest decorator
def test_login():
    print('in test loginpage')
class TestLoginPage():
    def test_display(self):
        print('in display method')
    def test_read(self):
        print('in test read method')



