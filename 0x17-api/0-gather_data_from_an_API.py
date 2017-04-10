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
    var root = 'https://jsonplaceholder.typicode.com';

    $.ajax({
        url: root + '/posts/1',
        method: 'GET'
    }).then(function(data) {
        console.log(data);
    });
