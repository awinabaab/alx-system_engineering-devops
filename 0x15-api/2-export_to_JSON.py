#!/usr/bin/python3
"""Gets information about a user's TODO list progress
from https://jsonplaceholder.typicode.com/ API
and exports it to a JSON file"""

import json
from requests import get
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    todos = get(f"{base_url}/todos?userId={userId}").json()
    employee_name = get(f"{base_url}/users?id={userId}"
                        ).json()[0].get('username')

    todo_list = []
    for todo in todos:
        new_todo = {}
        new_todo.update({"task": todo.get('title'),
                         "completed": todo.get('completed'),
                         "username": employee_name
                         })
        todo_list.append(new_todo)

    user_todos = {f"{userId}": todo_list}

    file_name = f"{userId}.json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(user_todos, file)
