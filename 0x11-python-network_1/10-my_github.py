#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv


if __name__ == "__main__":
    token = argv[2]
    url = 'https://api.github.com/user'
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(url, headers=headers, params=params)
    print(r.json().get("id"))
