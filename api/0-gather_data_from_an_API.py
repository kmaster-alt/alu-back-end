#!/usr/bin/python3
"""API"""
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    ).json()

    done = 0

    for t in todos:
        if t.get("completed") is True:
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done, len(todos)))

    for t in todos:
        if t.get("completed") is True:
            print("\t {}".format(t.get("title")))