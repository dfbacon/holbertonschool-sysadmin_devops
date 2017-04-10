#!/usr/bin/python3
'''

This is the '2-export_to_JSON' module.

1-export_to_CSV usesa dummy REST API to export data from
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
    import requests

    var root = 'https://jsonplaceholder.typicode.com';

    $.ajax({
        url: root + '/posts/1',
        method: 'GET'
    }).then(function(data) {
        console.log(data);
    });
