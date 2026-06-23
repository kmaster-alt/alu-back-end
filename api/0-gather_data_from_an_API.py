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

    done = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))

    for t in done:
        print("\t {}".format(t.get("title")))