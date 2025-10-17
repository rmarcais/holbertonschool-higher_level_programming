#!/usr/bin/python3
"""2-square.py
Write a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size

- Instantiation with optional size: def __init__(self, size=0):
. size must be an integer, otherwise raise a TypeError exception
 with the message size must be an integer.
. if size is less than 0, raise a ValueError
 exception with the message size must be >= 0.
- Public instance method: def area(self): that returns the current square area.
"""


class Square:
    """class that defines a square"""

    """The __init__ method is run as soon as the object class
    is instantiated.
    Args:
    size: The size of the square. It must be a positiv integer.
    Attribute:
    __size: Private instance attribute that is the size of the square.
    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
