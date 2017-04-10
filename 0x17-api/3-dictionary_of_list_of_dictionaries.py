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

if __name__ == "__main__":
    import requests

    var root = 'https://jsonplaceholder.typicode.com';

    $.ajax({
        url: root + '/posts/1',
        method: 'GET'
    }).then(function(data) {
        console.log(data);
    });
