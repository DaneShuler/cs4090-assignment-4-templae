Feature: Adding a Task
  Scenario: Successfully adding a new task
    Given an empty task list
    When I add a task titled "New BDD Task"
    Then the task list should contain "New BDD Task"


