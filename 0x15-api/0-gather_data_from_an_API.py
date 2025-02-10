#!/usr/bin/python3
"""Returns information about a user's TODO list progress
from https://jsonplaceholder.typicode.com/ API"""

from requests import get
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    todos = get(f"{base_url}/todos?userId={userId}").json()
    employee_name = get(f"{base_url}/users?id={userId}").json()[0].get('name')

    completed_todos = sum(1 for todo in todos if todo.get("completed"))
    total_todos = len(todos)

    print("Employee " + employee_name + " is done with tasks(" +
          str(completed_todos) + "/" + str(total_todos) + "):")

    completed_todos_list = [todo for todo in todos if todo.get('completed')]
    for todo in completed_todos_list:
        print(f"\t {todo.get('title')}")
