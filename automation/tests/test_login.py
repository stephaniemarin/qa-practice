from selenium import webdriver
from selenium.webdriver.common.by import By

def create_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver

def test_valid_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert"inventory.html" in driver.current_url
    
    driver.quit()
    
def test_invalid_password_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "Username and password do not match" in error_message
    
    driver.quit()
    
def test_locked_out_user_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    
    assert "locked out" in error_message
    
    driver.quit()
    
def test_empty_username_and_password():
    driver = create_driver()
    
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "Username is required" in error_message
    
    driver.quit()
    