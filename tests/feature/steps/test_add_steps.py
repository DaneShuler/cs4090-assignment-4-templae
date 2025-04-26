import pytest
from pytest_bdd import scenarios, given, when, then
from src.tasks import add_task, load_tasks, save_tasks

scenarios("../feature/add_task.feature")

@given("an empty task list")
def task_list(tmp_path):
    file_path = tmp_path / "tasks.json"
    save_tasks([], file_path)
    return file_path

@when('I add a task titled "New BDD Task"')
def add_new_task(task_list):
    tasks = load_tasks(task_list)
    add_task(tasks, "New BDD Task", "BDD testing task", "High", "2099-12-31", "Testing")

@then('the task list should contain "New BDD Task"')
def verify_task_added(task_list):
    tasks = load_tasks(task_list)
    assert any(task["title"] == "New BDD Task" for task in tasks)
