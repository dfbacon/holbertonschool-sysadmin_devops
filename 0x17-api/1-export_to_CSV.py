#!/usr/bin/python3
'''

This is the '1-export_to_CSV' module.

1-export_to_CSV usesa dummy REST API to export data from
'0-gather_data_from_an_API' in CSV format.

Additional Requirements:
* Records all tasks that are owned by a given employee.
* Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITTLE"
* File name must be: USER_ID.csv

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
