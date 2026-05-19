from selenium.webdriver.common.by import By

def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(username)
    driver.find_element(By.ID,"lodin-button").click()
    

def get_error_message(Driver):
    return driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text