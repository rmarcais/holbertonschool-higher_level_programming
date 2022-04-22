#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ =="__main__":
    if len(argv) < 2:
        d = {'q': ""}
    else:
        d = {'q': argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data=d)
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except Exception:
        print("Not a valid JSON")
