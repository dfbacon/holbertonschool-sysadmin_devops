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
import json
import requests
import sys


def get_user(uid):
    '''This is the 'get_user' method.

    Requests info from matching user id to API
    '''
    name = requests.get("{}/users/{}".format(
        url, sys.argv[1])).json().get("name")
    if name is None:
        return

    r = requests.get("{}/todos?userId={}".format(
        url, sys.argv[1])).json()
    completed = [e for e in r if e.get("completed") is True]
    print("Employee {} is done with tasks({:d}/{:d}):".format(
        name, len(completed), len(r)))

    if completed:
        print("\t ", end="")
        print("\n\t ".join(e.get("title") for e in completed))

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) > 1:
        try:
            uid = int(sys.argv[1])
            get_user(uid)

        except (ValueError, TypeError):
            pass
