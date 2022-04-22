#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import urllib.request
import urllib.error
from sys import argv

try:
    with urllib.request.urlopen(argv[1]) as r:
        print(r.read().decode('utf8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.status))
