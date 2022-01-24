#!/usr/bin/python3
"""0-rectangle.py
Write an empty class Rectangle that defines a rectangle

Private instance attribute: width:
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
. width must be an integer, otherwise raise a TypeError exception
 with the message width must be an integer
. if width is less than 0, raise a ValueError exception with
 the message width must be >= 0

Private instance attribute: height:
- property def height(self): to retrieve it
- property setter def height(self, value): to set it:
. height must be an integer, otherwise raise a TypeError
 exception with the message height must be an integer
. if height is less than 0, raise a ValueError
 exception with the message height must be >= 0

Instantiation with optional width and height:
 def __init__(self, width=0, height=0):
"""


class Rectangle:
    """Class that defines a rectangle"""

    """The __init__  method is run as soon as the object class
    is instantiated.
    Args:
    width: The width of the rectangle
    height: The height of the rectangle
    __width: private instance attribute: The width of the rectangle
    __height: private instance attribute: the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """property method
        Return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property method
        Args:
        value: The width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property method
        Return: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def height(self, value):
        """property method
        Args:
        value: The height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
