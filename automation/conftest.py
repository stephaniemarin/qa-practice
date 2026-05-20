import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com/"


#create driver
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(BASE_URL)
    
    yield browser
    
    browser.quit()