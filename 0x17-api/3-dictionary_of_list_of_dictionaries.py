#!/usr/bin/python3
'''

This is the '3-dictionary_of_list_of_dictionaries' module.

3-dictionary_of_list_of_dictionaries uses a dummy REST API to export data from
'0-gather_data_from_an_API' in JSON format.

Additional Requirements:
* Records all tasks from all employees.
* Formart must be: { "USER_ID": [ {"task": "TASK_TITTLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}},
    {"task": "TASK_TITTLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}}, ... ], USER_ID": [ {"task": "TASK_TITTLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}},
    {"task": "TASK_TITTLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}}, ... ]}
* File name must be: todo_all_employees.json

'''
import json
import requests


if __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(url).json()
        with open("todo_all_employees.json", mode="w", newline="") as f:
            json.dump({user.get("id"): [
                {"task": e.get("title"), "completed": e.get("completed"),
                 "username": user.get("username")} for e in requests.get(
                    "{}/{}/todos".format(url, user.get("id"))).json()
            ] for user in r}, f)
    except:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        pass
