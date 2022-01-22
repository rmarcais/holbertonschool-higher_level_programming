#!/usr/bin/python3
"""0-add_integer.py

Test file: 0-add_integer.txt

To test the function add_integer, run:
 python3 -m doctest -v ./tests/0-add_integer.txt | tail -2


Function: add_integer
"""


def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
    a: integer (or float)
    b: integer (or float), equal to 98
    Return:
    The addition of a and b
    """
    if (type(a) is not int and type(a) is not float) or a is None:
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float) or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
