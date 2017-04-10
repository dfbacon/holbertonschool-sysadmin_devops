#!/usr/bin/python3
'''

This is the '0-gather_data_from_an_API' module.

0-gather_data_from_an_API uses a given dummy REST API and returns information
about a given employee's TODO list progress.

Additional Requirements:
* Must accept an integer as a parameter (employee ID)
* Must display to stdout:
    * First line: Employee EMPLOYEE_NAME is done with
                  tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        * EMPLOYEE_NAME: name of the employee
        * NUMBER_OF_DONE_TASKS: number of completed tasks
        * TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
              sum of completed and non-completed tasks
    * Second and N next lines display the tittle of completed tasks:
        Tab TASK_TITTLE

'''
if __name__ == "__main__":
    import requests
    import json
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py employee_id")
        exit(1)

    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    user_id = int(sys.argv[1])

    try:
        r_users = requests.get(url_users)
        r_todo = requests.get(url_todo)
        total_count = 0
        completed_count = 0

        for user in r_users.json():
            if user['id'] is user_id:
                user_name = user['name']

        for task in r_todo.json():
            if task['userId'] is user_id:
                total_count += 1
                if task['completed'] is True:
                    completed_count += 1

        print("Employee {} is done with tasks({}/{}):".format(
            user_name, completed_count, total_count))

        for task_name in r_todo.json():
            if task_name['userId'] is user_id:
                if task_name['completed'] is True:
                    print("\t{}".format(task_name['title']))

    except:
        pass
