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
    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users"
    if len(sys.argv) > 1:
        name = requests.get("{}/{}".format(
            url, sys.argv[1])).json().get("username")
        r_todo = requests.get("{}/{}/todos".format(
            url, sys.argv[1])).json()

        with open("{}.csv".format(sys.argv[1]), mode="w", newline="") as f:
            writer = csv.writer(f, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows([sys.argv[1], name,
                              e.get("completed"),
                              e.get("title")] for e in r_todo)
