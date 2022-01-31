#!/usr/bin/python3
"""9-rectangle.py
Classes: BaseGeometry (base class), Rectangle (subclass) and Square (subclass).
Method(s) of BaseGeometry: area, integer_validator
Method(s) of Rectangle: __init__, area and str
Method(s) of Square: __init__, area
"""


class BaseGeometry:
    """class containing two methods: area and integer_validator."""
    def area(self):
        """raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value (which must be an integer)."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
