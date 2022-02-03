#!/usr/bin/python3
"""rectangle.py
Module that defines a class Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """Class called Rectangle that inherits from Base."""

    """The __init__ method is called when a new instance is created.
    Args:
    width
    height
    x
    y
    id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """public getter method."""
        return self.__width

    @width.setter
    def width(self, width):
        """public setter method."""
        self.__width = width

    @property
    def height(self):
        """public getter method."""
        return self.__height

    @height.setter
    def height(self, height):
        """public setter method."""
        self.__height = height

    @property
    def x(self):
        """public getter method."""
        return self.__x

    @x.setter
    def x(self, x):
        """public setter method."""
        self.__x = x

    @property
    def y(self):
        """public getter method."""
        return self.__y

    @y.setter
    def y(self, y):
        """public setter method."""
        self.__y = y
