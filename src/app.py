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

# Unit Testing (test_basic.py)
if st.button("Run Unit Tests (test_basic.py)"):
    output = run_test_command("pytest tests/test_basic.py --cov=src --cov-report=term-missing")
    st.code(output)

# Advanced Testing Features (test_advanced.py)
if st.button("Run Advanced Tests (Parameterized, Fixtures, Mocking)"):
    output = run_test_command("pytest tests/test_advanced.py")
    st.code(output)

# Property-Based Testing (test_property.py)
if st.button("Run Property-Based Tests (test_property.py)"):
    output = run_test_command("pytest tests/test_property.py")
    st.code(output)

# TDD Testing (test_tdd.py)
if st.button("Run TDD Tests (test_tdd.py)"):
    output = run_test_command("pytest tests/test_tdd.py")
    st.code(output)

# HTML Report Generation
if st.button("Generate HTML Report"):
    output = run_test_command("pytest --html=report.html")
    st.code(output)
    st.markdown("✅ HTML Report generated: `report.html` (Check project folder)")

st.markdown("---")
st.caption("CS4090 To-Do App Testing Assignment")
