#!/usr/bin/python3
"""9-rectangle.py
Classes: BaseGeometry (base class) and Rectangle (subclass).
Method(s) of BaseGeometry: area, integer_validator
Method(s) of Rectangle: __init__, area and __str__
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry."""

    """The __init__ method, that is called whena new instance is created."""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Tells the main program how to print Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
