import pytest
from unittest.mock import patch
from src.tasks import (
    generate_unique_id,
    filter_tasks_by_priority,
    save_tasks
)

# --------------------------
# Fixtures Example
# --------------------------
@pytest.fixture
def task_list():
    return [
        {"id": 1, "priority": "High"},
        {"id": 2, "priority": "Low"},
        {"id": 3, "priority": "Medium"},
        {"id": 4, "priority": "High"},
    ]

# --------------------------
# Parameterized Test Example
# --------------------------
@pytest.mark.parametrize("priority,expected_count", [
    ("High", 2),
    ("Medium", 1),
    ("Low", 1),
    ("None", 0)
])
def test_filter_priority_param(task_list, priority, expected_count):
    filtered = filter_tasks_by_priority(task_list, priority)
    assert len(filtered) == expected_count

# --------------------------
# Fixture Usage Test
# --------------------------
def test_generate_id_with_fixture(task_list):
    assert generate_unique_id(task_list) == 5

# --------------------------
# Mocking Example
# --------------------------
def test_save_tasks_mock(tmp_path):
    test_tasks = [{"id": 1, "title": "Mock Task"}]
    test_file = tmp_path / "mock_tasks.json"
    
    with patch("builtins.open", create=True) as mocked_open:
        save_tasks(test_tasks, test_file)
        assert mocked_open.called
