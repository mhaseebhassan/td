from selenium.webdriver.common.by import By

def test_01_login_page_loads(driver, base_url, wait_for):
    driver.get(f"{base_url}/login")
    assert wait_for(driver, By.ID, "username")
    assert wait_for(driver, By.ID, "password")
    assert wait_for(driver, By.ID, "login-btn")
    assert "Login" in driver.title or "login" in driver.current_url
