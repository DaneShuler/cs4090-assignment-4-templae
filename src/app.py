import streamlit as st
import subprocess
from tasks import (
    load_tasks, save_tasks, add_task, delete_task, mark_task_complete,
    filter_tasks_by_priority, filter_tasks_by_category, filter_tasks_by_completion,
    search_tasks, get_overdue_tasks, archive_completed_tasks, add_recurring_task
)

# Streamlit App Title
st.title("✅ To-Do List Application with Testing Features")

# Load existing tasks
tasks = load_tasks()

# -------------------------------
# Task Management Section
# -------------------------------
st.header("Manage Tasks")

title = st.text_input("Task Title")
description = st.text_area("Task Description")
priority = st.selectbox("Priority", ["High", "Medium", "Low"])
due_date = st.date_input("Due Date")
category = st.text_input("Category")

if st.button("Add Task"):
    add_task(tasks, title, description, priority, due_date.strftime("%Y-%m-%d"), category)
    st.success("Task added!")

if st.button("Archive Completed Tasks"):
    archive_completed_tasks(tasks)
    st.success("Completed tasks archived!")

# Display tasks
st.subheader("Current Tasks")
for task in tasks:
    st.write(task)

# -------------------------------
# TESTING BUTTONS SECTION
# -------------------------------
st.header("🧪 Run Tests")

def run_test_command(command):
    """Helper function to run subprocess command and capture output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + "\n" + result.stderr

if st.button("Run Unit Tests"):
    output = run_test_command("pytest tests/test_unit.py --cov=src --cov-report=term-missing")
    st.code(output)

if st.button("Run Parameterized Tests"):
    output = run_test_command("pytest tests/test_parameterized.py")
    st.code(output)

if st.button("Run Fixture Tests"):
    output = run_test_command("pytest tests/test_fixtures.py")
    st.code(output)

if st.button("Run Mocking Tests"):
    output = run_test_command("pytest tests/test_mocking.py")
    st.code(output)

if st.button("Generate HTML Report"):
    output = run_test_command("pytest --html=report.html")
    st.code(output)
    st.markdown("✅ HTML Report generated: `report.html` (Check project folder)")

if st.button("Run TDD Tests"):
