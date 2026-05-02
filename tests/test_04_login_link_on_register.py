from selenium.webdriver.common.by import By

def test_04_login_link_on_register(driver, base_url, wait_for, wait_clickable):
    driver.get(f"{base_url}/register")
    link = wait_clickable(driver, By.ID, "login-link")
    link.click()
    wait_for(driver, By.ID, "login-btn")
    assert "login" in driver.current_url
