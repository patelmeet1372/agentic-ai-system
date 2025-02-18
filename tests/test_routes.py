from app.utils import create_task, update_task, delete_task

def test_create_task():
    task = create_task("Finish the report", "high")
    assert task["description"] == "Finish the report"
    assert task["priority"] == "high"

def test_update_task():
    create_task("Finish the report")
    updated_task = update_task(0, completed=True)
    assert updated_task["completed"] is True

def test_delete_task():
    create_task("Finish the report")
    deleted_task = delete_task(0)
    assert deleted_task["description"] == "Finish the report"

