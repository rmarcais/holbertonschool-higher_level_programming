#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response.
"""


if __name__ == "__main__":
    import urllib.request as u
    from sys import argv

    req = u.Request(argv[1])
    with u.urlopen(req) as r:
        for i in r.getheaders():
            if i[0] == "X-Request-Id":
                print(i[1])
                break
