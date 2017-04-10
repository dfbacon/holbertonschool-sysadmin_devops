#!/usr/bin/python3
'''

This is the '2-export_to_JSON' module.

2-export_to_JSON uses a dummy REST API to export data from
'0-gather_data_from_an_API' in JSON format.

Additional Requirements:
* Records all tasks tat are owned by a given employee.
* Formart must be: { "USER_ID": [ {"task": "TASK_TITTLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}},
    {"task": "TASK_TITTLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}}, ... ]}
* File name must be: USER_ID.json

'''

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py employee_id")
        exit(1)

    try:
        url = "https://jsonplaceholder.typicode.com/users"
        user_name = requests.get("{}/{}".format(
            url, sys.argv[1])).json().get("username")
        r_todo = requests.get("{}/{}/todos".format(
            url, sys.argv[1])).json()
        with open("{}.json".format(sys.argv[1]), mode="w", newline="") as f:
            json.dump({sys.argv[1]: [
                {"task": e.get("title"), "completed": e.get("completed"),
                 "username": user_name} for e in r_todo]}, f)
    except:
        pass
