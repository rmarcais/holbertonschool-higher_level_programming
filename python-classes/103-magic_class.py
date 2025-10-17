#!/usr/bin/python3
"""103-magic_class.py"""
import math
"""Imports the module math to compute the area and
 the circomference of a circle
"""


class MagicClass:
    """Class that defines a circle"""

    """Initialization of the circle"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Computes the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Computes the circomference of the circle"""
        return (2 * math.pi * self.__radius)
