#!/usr/bin/python3
""" This script fetches https://intranet.hbtn.io/status """


import urllib.request as u

if __name__ == "__main__":
    with u.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
