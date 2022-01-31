#!/usr/bin/python3
"""7-base_geometry
You are not allowed to import any module.

Test file: 7-base_geometry.txt
Class: BaseGeometry
Method(s): area, integer_validator
To do some tests, run: python3 -m doctest ./test/7-base_geometry.txt
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
