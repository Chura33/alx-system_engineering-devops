#!/usr/bin/python3
""" This module  display on the standard output the employee
    TODO list progress in this exact format:
    - Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks,
    which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed
    tasks: TASK_TITLE (with 1 tabulation
    and 1 space before the TASK_TITLE)
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0
    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1
    print(
            "Employee {} is done with tasks({}/{}):".format(
                        name, totalTasks, len(json_req)
                            )
            )
    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
