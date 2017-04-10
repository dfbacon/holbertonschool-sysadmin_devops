#!/usr/bin/python3
'''

This is the '1-export_to_CSV' module.

1-export_to_CSV usesa dummy REST API to export data from
'0-gather_data_from_an_API' in Comma Separated Values (CSV) format.

Additional Requirements:
* Records all tasks that are owned by a given employee.
* Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITTLE"
* File name must be: USER_ID.csv

'''

if __name__ == "__main__":
    import requests
    import json
    import csv
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py employee_id")
        exit(1)

    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    user_id = int(sys.argv[1])

    try:
        r_users = requests.get(url_users)
        r_todo = requests.get(url_todo)
        file_name = str(user_id) + '.csv'

        for user in r_users.json():
            if user['id'] is user_id:
                user_name = user['name']

        with open(file_name, 'w+', newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for row in r_todo.json():
                if row['userId'] is user_id:
                    writer.writerows(row['userId'], user_name,
                                     row['completed'], row['title'])

    except:
        pass
