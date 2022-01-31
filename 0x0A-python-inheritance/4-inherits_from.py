#!/usr/bin/python3
"""4-inherits_from.py
You are not allowed to import any module.
Function: is_kind_of_class.
"""


def inherits_from(obj, a_class):
    """Function that returns True is the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise Flase.
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
