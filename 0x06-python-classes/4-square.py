#!/usr/bin/python3
"""4-square.py
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
- property def size(self): to retrieve it

- property setter def size(self, value): to set it:
. size must be an integer, otherwise raise a
  TypeError exception with the message size must be an integer
. if size is less than 0, raise a ValueError
 exception with the message size must be >= 0

- Instantiation with optional size: def __init__(self, size=0):

- Public instance method: def area(self): that returns the current square area
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

    @property
    def size(self):
        """property method

        Returns: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property method

        Args:
        size: The new size of the square which must be a positiv integer.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
