#!/usr/bin/python3
"""Gets information about a user's TODO list progress
from https://jsonplaceholder.typicode.com/ API
and exports it to a JSON file"""

import json
from requests import get


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    employees = get(f"{base_url}/users").json()
    user_todos = {}

    for employee in employees:
        employee_name = employee.get('username')
        employee_id = employee.get('id')

        todos = get(f"{base_url}/todos?userId={employee_id}").json()
        todo_list = []

        for todo in todos:
            new_todo = {"username": employee_name,
                        "task": todo.get('title'),
                        "completed": todo.get('completed'),
                        }
            todo_list.append(new_todo)

        user_todos.update({employee_id: todo_list})

    file_name = "todo_all_employees.json"
    with open(file_name, "a", encoding="utf-8") as file:
        json.dump(user_todos, file)
