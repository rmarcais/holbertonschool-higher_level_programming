#!/usr/bin/python3
"""3-is_kind_of_class.py
You are not allowed to import any module.
Function: is_same_class.
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True is the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise Flase.
    """
    return isinstance(obj, a_class)
