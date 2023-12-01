import pytest
import sys

@pytest.mark.skip
def test_Login():
    print("Login")


@pytest.mark.skipif(sys.version_info<(3,9),reason="Python version not supported")
def test_AddProduct():
    print("Add Product")

@pytest.mark.xfail
def test_Logout():
    assert False
    print("Logout done")


def test_closeApplication():
    assert True
    print("Close the application")