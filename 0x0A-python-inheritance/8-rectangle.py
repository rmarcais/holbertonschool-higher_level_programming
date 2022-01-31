#!/usr/bin/python3
"""8-rectangle.py
Classes: BaseGeometry (base class) and Rectangle (subclass).
Method(s) of BaseGeometry: area, integer_validator
Method(s) of Rectangle: __init__
"""


"""class BaseGeometry:
    ""class containing two methods: area and integer_validator.""
    def area(self):
        ""raises an Exception with the message 'area() is not implemented'.""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ""Method that validates value (which must be an integer).""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherits from BaseGeometry."""

    """The __init__ method, that is called when a new instance is created,
    takes as parameters the width and the height of the rectangle."""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
