#!/usr/bin/python3
"""9-rectangle.py
Classes: BaseGeometry (base class), Rectangle (subclass) and Square (subclass).
Method(s) of BaseGeometry: area, integer_validator
Method(s) of Rectangle: __init__, area and str
Method(s) of Square: __init__, area
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle."""

    """__init__ method that is called when a new instance is created."""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of a square."""
        return self.__size ** 2
