#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        data = response.json()
        print(data.get("id", "None"))
    except ValueError:
        print("None")
