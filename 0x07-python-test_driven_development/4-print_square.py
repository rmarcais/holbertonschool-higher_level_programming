#!/usr/bin/python3
"""4-print_square.py

Test file: 4-print_square.txt

To test the function print_square, run:
python3 -m doctest -v ./tests/4-print_square.txt


Function:
print_square
"""


def print_square(size):
    """Function that prints a quare with the character #
    Args:
    size: The size length of the square
    Return:
    Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
