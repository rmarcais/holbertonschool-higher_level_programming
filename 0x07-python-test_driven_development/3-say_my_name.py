#!/usr/bin/python3
"""3-say_my_name.py

Test file: 3-say_my_name.txt

To test the function say_my_name, run:
python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2


Function: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>.
    Args:
    fisrt_name: The first name of the person (string)
    last_name: The last_name of the person (string), equal to ""
    Return:
    Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
