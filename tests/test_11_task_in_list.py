from selenium.webdriver.common.by import By

def test_11_task_in_list(driver, wait_for):
    todo_list = wait_for(driver, By.ID, "todo-list")
    assert "Buy groceries" in todo_list.text
