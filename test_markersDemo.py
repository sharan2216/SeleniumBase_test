import pytest

@pytest.mark.smoke
def test_Login():
    print("Login")


@pytest.mark.regression
def test_AddProduct():
    print("Add Product")


@pytest.mark.smoke
def test_Logout():
    print("Login")