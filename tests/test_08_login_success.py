from selenium.webdriver.common.by import By

def test_08_login_success(driver, base_url, test_user, test_pass, wait_for):
    driver.get(f"{base_url}/login")
    wait_for(driver, By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(test_user)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(test_pass)
    driver.find_element(By.ID, "login-btn").click()

    wait_for(driver, By.ID, "task-input")
    assert driver.current_url.rstrip("/") == base_url \
        or driver.current_url.rstrip("/").endswith("/")
