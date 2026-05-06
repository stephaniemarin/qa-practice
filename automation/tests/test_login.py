from selenium import webdriver
from selenium.webdriver.common.by import By

#create driver
def create_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver

#valid login
def test_valid_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert"inventory.html" in driver.current_url
    
    driver.quit()

#invalid password
def test_invalid_password_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "Username and password do not match" in error_message
    
    driver.quit()

#locked out user login
def test_locked_out_user_login():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    
    assert "locked out" in error_message
    
    driver.quit()

#empty username and password
def test_empty_username_and_password():
    driver = create_driver()
    
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "Username is required" in error_message
    
    driver.quit()

#whitespace username
def test_whitespace_username():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys(" ")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    
    driver.quit()
    
#long username
def test_long_username():
    driver = create_driver()
    
    long_username = "a" * 300
    
    driver.find_element(By.ID, "user-name").send_keys(long_username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    
    assert "Username and password do not match" in error_message
    
    driver.quit()
    
#special characters
def test_special_characters_username():
    driver = create_driver()
    
    driver.find_element(By.ID, "user-name").send_keys("@@@###")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    
    assert "Username and password do not match" in error_message
    
    driver.quit()