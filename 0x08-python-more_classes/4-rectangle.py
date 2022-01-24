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
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self):
 that returns the rectangle perimeter:
. if width or height is equal to 0, perimeter is equal to 0
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

    @height.setter
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

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method taht returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """This method tells the main program how to print a rectangle"""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                if i != self.__height - 1:
                    print()
        return ""

    def __repr__(self):
        """Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)
