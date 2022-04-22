#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge:
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    r = requests.get(url)
    for i in range(10):
        sha = r.json()[i].get("sha")
        aname = r.json()[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, aname))
