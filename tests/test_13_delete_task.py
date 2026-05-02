from selenium.webdriver.common.by import By

def test_13_delete_task(driver, wait_for, wait_clickable):
    todo_list = wait_for(driver, By.ID, "todo-list")
    items = todo_list.find_elements(By.CSS_SELECTOR, ".todo-item")
    assert len(items) > 0

    first_item = items[0]
    item_id = first_item.get_attribute("id").replace("todo-", "")
    delete_btn = wait_clickable(driver, By.ID, f"delete-{item_id}")
    delete_btn.click()

    wait_for(driver, By.ID, "todo-list")
