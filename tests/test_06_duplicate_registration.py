from selenium.webdriver.common.by import By

def test_06_duplicate_registration(driver, base_url, test_user, test_pass, wait_for):
    driver.get(f"{base_url}/register")
    wait_for(driver, By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(test_user)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(test_pass)
    driver.find_element(By.ID, "register-btn").click()

    wait_for(driver, By.CSS_SELECTOR, ".flash.error")
    body = driver.find_element(By.TAG_NAME, "body").text
    assert "already exists" in body
