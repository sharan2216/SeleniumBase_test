import pytest
import sys


@pytest.mark.parametrize("username,password",
                         [
                             ("Selenium","Webdriver"),
                             ("Python","pytest"),
                             ("Mukesh","otwani")
                         ]
                         )

def test_Login(username,password):
    print(username)
    print(password)