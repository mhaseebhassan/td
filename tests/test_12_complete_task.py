from selenium.webdriver.common.by import By

def test_12_complete_task(driver, wait_for, wait_clickable):
    todo_list = wait_for(driver, By.ID, "todo-list")
    items = todo_list.find_elements(By.CSS_SELECTOR, ".todo-item")
    assert len(items) > 0

    first_item = items[0]
    item_id = first_item.get_attribute("id").replace("todo-", "")
    complete_btn = wait_clickable(driver, By.ID, f"complete-{item_id}")
    complete_btn.click()

    completed_span = wait_for(driver, By.CSS_SELECTOR, f"#todo-{item_id} .completed")
    assert completed_span is not None
