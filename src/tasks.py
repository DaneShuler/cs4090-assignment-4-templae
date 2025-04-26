import json
import os
from datetime import datetime

DEFAULT_TASKS_FILE = "tasks.json"

def load_tasks(file_path=DEFAULT_TASKS_FILE):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks, file_path=DEFAULT_TASKS_FILE):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)

def generate_unique_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1

def filter_tasks_by_priority(tasks, priority):
    return [task for task in tasks if task.get("priority") == priority]

def filter_tasks_by_category(tasks, category):
    return [task for task in tasks if task.get("category") == category]

def filter_tasks_by_completion(tasks, completed=True):
    return [task for task in tasks if task.get("completed") == completed]

def search_tasks(tasks, query):
    query = query.lower()
    return [
        task for task in tasks
        if query in task.get("title", "").lower() or query in task.get("description", "").lower()
    ]

def get_overdue_tasks(tasks):
    today = datetime.now().date()
    overdue = []
    for task in tasks:
        due_date = task.get("due_date")
        if due_date and not task.get("completed"):
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
            if due_date_obj < today:
                overdue.append(task)
    return overdue

def add_task(tasks, title, description, priority, due_date, category):
    new_task = {
        "id": generate_unique_id(tasks),
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "category": category,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def delete_task(tasks, task_id):
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return tasks

def mark_task_complete(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(tasks)
    return tasks

def archive_completed_tasks(tasks):
    tasks = [task for task in tasks if not task.get("completed")]
    save_tasks(tasks)
    return tasks

def add_recurring_task(tasks, title, description, priority, due_date, category, recurrence_days):
    new_task = add_task(tasks, title, description, priority, due_date, category)
    new_task["recurrence_days"] = recurrence_days
    save_tasks(tasks)
    return new_task
