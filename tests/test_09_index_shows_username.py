from selenium.webdriver.common.by import By

def test_09_index_shows_username(driver, test_user, wait_for):
    wait_for(driver, By.ID, "task-input")
    body = driver.find_element(By.TAG_NAME, "body").text
    assert test_user in body
