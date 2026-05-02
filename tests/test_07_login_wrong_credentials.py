from selenium.webdriver.common.by import By

def test_07_login_wrong_credentials(driver, base_url, test_user, wait_for):
    driver.get(f"{base_url}/login")
    wait_for(driver, By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(test_user)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-btn").click()

    assert "/login" in driver.current_url
