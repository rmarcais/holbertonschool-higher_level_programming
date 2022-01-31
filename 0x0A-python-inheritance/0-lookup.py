#!/usr/bin/python3
"""0-lookup.py
You are not allowed to import any module.
Function: lookup.
"""


def lookup(obj):
    """function that returns the list of available attributes
    and method of an object.
    """
    return dir(obj)
