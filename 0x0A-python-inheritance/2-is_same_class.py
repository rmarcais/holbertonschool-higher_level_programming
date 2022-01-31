#!/usr/bin/python3
"""2-is_same_class.py
You are not allowed to import any module.
Function: is_same_class.
"""


def is_same_class(obj, a_class):
    """Function that returns True is the object is exactly an instance
    of the specified class; otherwise False.
    """
    return type(obj) is a_class
