#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Subclass of Shape"""

    def __init__(self, radius):
        """Initialization"""
        self.radius = radius

    def area(self):
        return pi * (self.radius**2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Subclass of Shape"""

    def __init__(self, width, height):
        """Initialization"""
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


def shape_info(shape):
    """
    Standalone function that accepts an object of type Shape
    and prints its area and permieter.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
