#!/usr/bin/python3
"""101-add_attribute.py
You are not allowed to import any module.
Function: add_attribute
"""


def add_attribute(a_class, attribute, value):
    """Function that adds a new attribute to an object if it's possible."""
    try:
        setattr(a_class, attribute, value)
    except Exception:
        raise TypeError("can't add new attribute")
