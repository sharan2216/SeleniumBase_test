from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import pytest


@pytest.fixture()
def setup():
    print("start Browser")
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")



def test_1(setup):
    driver.get("https://www.google.com/")
    print("Test 1 executed")


def test_2(setup):
    driver.get("https://www.cricbuzz.com/")
    print("Test 2 executed")

def test_3(setup):

    driver.get("https://www.oracle.com/")
    print("Test 3 executed")
