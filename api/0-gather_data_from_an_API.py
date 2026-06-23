#!/usr/bin/python3
"""API"""
import requests
import sys

if __name__ == "__main__":
    u = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(u)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(u)
    ).json()

    done = 0
    total = len(todos)

    for t in todos:
        if t.get("completed"):
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done, total))

    for t in todos:
        if t.get("completed"):
            print("\t {}".format(t.get("title")))