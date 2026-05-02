from selenium.webdriver.common.by import By

def test_02_register_page_loads(driver, base_url, wait_for):
    driver.get(f"{base_url}/register")
    assert wait_for(driver, By.ID, "username")
    assert wait_for(driver, By.ID, "password")
    assert wait_for(driver, By.ID, "register-btn")
    assert "Register" in driver.title or "register" in driver.current_url
