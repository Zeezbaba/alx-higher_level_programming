#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner,
                                                              repository)

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha", "")
            author_name = commit.get("commit", {}).\
                get("author", {}).get("name", "")
            print("{}: {}".format(sha, author_name))
    except ValueError:
        print("Error: Unable to fetch commits.")
