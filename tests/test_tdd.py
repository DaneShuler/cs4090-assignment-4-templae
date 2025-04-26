import pytest
from src.tasks import (
    get_overdue_tasks, archive_completed_tasks, add_recurring_task
)
from datetime import datetime, timedelta

@pytest.fixture
def overdue_tasks():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return [
        {"id": 1, "title": "Past Task", "due_date": yesterday, "completed": False},
        {"id": 2, "title": "Future Task", "due_date": tomorrow, "completed": False}
    ]

def test_overdue_task_detection(overdue_tasks):
    overdue = get_overdue_tasks(overdue_tasks)
    assert len(overdue) == 1
    assert overdue[0]["title"] == "Past Task"

def test_archive_completed_tasks():
    tasks = [
        {"id": 1, "completed": True},
        {"id": 2, "completed": False}
    ]
    remaining = archive_completed_tasks(tasks)
    assert len(remaining) == 1
    assert remaining[0]["id"] == 2

def test_add_recurring_task():
    tasks = []
    task = add_recurring_task(
        tasks, "Recurring Task", "Repeat every week", "High",
        due_date="2099-12-31", category="Work", recurrence_days=7
    )
    assert "recurrence_days" in task
    assert task["recurrence_days"] == 7
