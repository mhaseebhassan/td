from selenium.webdriver.common.by import By

def test_10_add_todo(driver, wait_for):
    task_input = wait_for(driver, By.ID, "task-input")
    task_input.clear()
    task_input.send_keys("Buy groceries")
    driver.find_element(By.ID, "add-btn").click()
    wait_for(driver, By.ID, "task-input")
