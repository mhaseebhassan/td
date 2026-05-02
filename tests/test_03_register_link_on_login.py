from selenium.webdriver.common.by import By

def test_03_register_link_on_login(driver, base_url, wait_for, wait_clickable):
    driver.get(f"{base_url}/login")
    link = wait_clickable(driver, By.ID, "register-link")
    link.click()
    wait_for(driver, By.ID, "register-btn")
    assert "register" in driver.current_url
