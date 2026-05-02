from selenium.webdriver.common.by import By

def test_14_deleted_task_gone(driver, wait_for):
    todo_list = wait_for(driver, By.ID, "todo-list")
    assert "Buy groceries" not in todo_list.text
