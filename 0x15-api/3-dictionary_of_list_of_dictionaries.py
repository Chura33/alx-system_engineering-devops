#!/usr/bin/python3
""" This script gets information of all users
and puts them in a json file
"""


import requests
from sys import argv
import json


if __name__ == '__main__':

    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                taskList.append({
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                    })
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
