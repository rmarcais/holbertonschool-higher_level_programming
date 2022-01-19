#!/usr/bin/python3
"""5-square.py
Write a class Square that defines a square by: (based on 4-square.py)

- Private instance attribute: size:
-- property def size(self): to retrieve it

-- property setter def size(self, value): to set it:
. size must be an integer, otherwise raise a
  TypeError exception with the message size must be an integer
. if size is less than 0, raise a ValueError
 exception with the message size must be >= 0

- Private instance attribute: position:
-- property def position(self): to retrieve it

-- property setter def position(self, value): to set it:
. position must be a tuple of 2 positive integers, otherwise raise a TypeError
 exception with the message position must be a tuple of 2 positive integers

- Instantiation with optional size and optional position:
 def __init__(self, size=0, position=(0, 0)):

- Public instance method: def area(self): that returns the current square area

- Public instance method: def my_print(self):
 that prints in stdout the square with the character #:
-- if size is equal to 0, print an empty line

-- position should be use by using space -
 Don’t fill lines by spaces when position[1] > 0
"""


class Square:
    """class that defines a square"""

    """The __init__ method is run as soon as the object class
    is instantiated.
    Args:
    size: The size of the square. It must be a positiv integer.
    position: The position of the square. It must be a tuple composed of
    2 positiv integers.
    Attribute:
    __size: Private instance attribute which means the size of the square.
    __position: Private instance attribute which means
    the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """property method
        Returns: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """property method
        Args:
        size: The new size of the square which must be a positiv integer.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """property method"""
        return self.__position

    @position.setter
    def position(self, value):
        """property method

        Args:
        value: The values of the position.
        """
        self.__position = value
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method prints in stdout the square with the character #."""

        if self.__size == 0:
            print("")
            return
        for a in range(0, self.__position[1]):
            print("")
        else:
            for i in range(0, self.__size):
                for b in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
