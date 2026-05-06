import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/")
#valid password
VALID_PASSWORD = "secret_sauce"

#create driver
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(BASE_URL)
    yield browser
    browser.quit()

def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys("username")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "login-button").click()
    
def get_error_message(driver):
    return driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text


#valid login
def test_valid_login(driver):
    login(driver, "standard_user", VALID_PASSWORD)
    
    assert"inventory.html" in driver.current_url


#invalid password
def test_invalid_password_login(driver):
    login(driver,"standard_user", "wrong_password")
 
    assert "Username and password do not match" in error_message(driver)
    

#locked out user login
def test_locked_out_user_login(driver):
    login(driver,"locked_out_user",VALID_PASSWORD)
    
    assert "locked out" in error_message(driver)
    


#empty username and password
def test_empty_username_and_password(driver):
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "Username is required" in error_message(driver)
    

#whitespace username
def test_whitespace_username(driver):
    login(driver, " ", VALID_PASSWORD)
    
    
    assert "Epic sadface: Username and password do not match any user in this service" in error_message(driver)
    
    
#long username
def test_long_username(driver):
 
    long_username = "a" * 300
    
    login(driver, long_username, VALID_PASSWORD)
    
    assert "Username and password do not match" in error_message(driver)
    
    
#special characters
def test_special_characters_username(driver):
    login(driver, "@@@###", VALID_PASSWORD)
    
    assert "Username and password do not match" in error_message(driver)
    