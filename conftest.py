# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Test başlamadan önce:
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # Test burada çalışır
    # Test bittikten sonra:
    driver.quit()