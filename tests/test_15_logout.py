from selenium.webdriver.common.by import By

def test_15_logout(driver, wait_for, wait_clickable):
    logout_btn = wait_clickable(driver, By.ID, "logout-btn")
    logout_btn.click()
    wait_for(driver, By.ID, "login-btn")
    assert "login" in driver.current_url
