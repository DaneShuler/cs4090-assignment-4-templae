import pytest
import os
import json
from src.tasks import (
    load_tasks,
    save_tasks,
    generate_unique_id,
    filter_tasks_by_priority,
    filter_tasks_by_completion,
)

@pytest.fixture
def sample_tasks():
    return [
        {"id": 1, "title": "Task 1", "priority": "High", "completed": True},
        {"id": 2, "title": "Task 2", "priority": "Low", "completed": False},
        {"id": 3, "title": "Task 3", "priority": "Medium", "completed": True},
        {"id": 4, "title": "Task 4", "priority": "High", "completed": False},
    ]

def test_generate_unique_id(sample_tasks):
    assert generate_unique_id(sample_tasks) == 5

def test_filter_by_priority(sample_tasks):
    high_tasks = filter_tasks_by_priority(sample_tasks, "High")
    assert len(high_tasks) == 2
    assert all(task["priority"] == "High" for task in high_tasks)

def test_filter_by_completion_true(sample_tasks):
    completed = filter_tasks_by_completion(sample_tasks, True)
    assert len(completed) == 2
    assert all(task["completed"] for task in completed)

def test_filter_by_completion_false(sample_tasks):
    incomplete = filter_tasks_by_completion(sample_tasks, False)
    assert len(incomplete) == 2
    assert all(not task["completed"] for task in incomplete)

def test_save_and_load_tasks(tmp_path):
    test_path = tmp_path / "tasks.json"
    original = [{"id": 99, "title": "Test Save"}]
    save_tasks(original, test_path)
    loaded = load_tasks(test_path)
    assert loaded == original
