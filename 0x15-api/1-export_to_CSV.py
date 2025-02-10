#!/usr/bin/python3
"""Returns information about a user's TODO list progress
from https://jsonplaceholder.typicode.com/ API
and exports it to a CSV file"""

import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    todos = get(f"{base_url}/todos?userId={userId}").json()
    employee_name = get(f"{base_url}/users?id={userId}"
                        ).json()[0].get('username')

    file_name = f"{userId}.csv"

    todo_list = []
    for todo in todos:
        new_todo = {}
        new_todo.update({'user_id': userId,
                         'name': employee_name,
                         'task_completed': todo.get('completed'),
                         'task_title': todo.get('title')
                         })
        todo_list.append(new_todo)

    with open(file_name, "w", encoding="utf-8") as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow(todo.values())
