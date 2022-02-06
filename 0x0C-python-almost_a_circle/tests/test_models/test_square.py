#!/usr/bin/python3
"""
Add unit test for the class Square.
"""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquareAttributes(unittest.TestCase):
    """Class that tests the methods of the class Square."""

    def test_square_negative_size(self):
        """Test creating a Square instance with a negative size."""
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_square_negative_x(self):
        """Test creating a Square instance with a negative x."""
        with self.assertRaises(ValueError):
            s1 = Square(5, -1)

    def test_square_negative_y(self):
        """Test creating a Square instance with a negative y."""
        with self.assertRaises(ValueError):
            s1 = Square(5, 1, -1)

    def test_square_string_size(self):
        """Test creating a Square instance with size as a string."""
        with self.assertRaises(TypeError):
            s1 = Square("hello")

    def test_square_string_x(self):
        """Test creating a Square instance with x as a string."""
        with self.assertRaises(TypeError):
            s1 = Square(5, "hello")

    def test_square_string_y(self):
        """Test creating a Square instance with y as a string."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, "hello")

    def test_square_zero_size(self):
        """Test creating a Square instance with size equal to 0."""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_square_float_size(self):
        """Test creating a Square instance with size as a float."""
        with self.assertRaises(TypeError):
            s1 = Square(5.1)

    def test_square_float_x(self):
        """Test creating a Square instance with x as a float."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1.1)

    def test_square_float_y(self):
        """Test creating a Square instance with y as a float."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, 1.1)

    def test_square_list_size(self):
        """Test creating a Square instance with size as a list."""
        with self.assertRaises(TypeError):
            s1 = Square([1, 2, 3])

    def test_square_list_x(self):
        """Test creating a Square instance with x as a list."""
        with self.assertRaises(TypeError):
            s1 = Square(5, [1, 2, 3])

    def test_square_list_y(self):
        """Test creating a Square instance with x as a list."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, [1, 2, 3])

    def test_square_tuple_size(self):
        """Test creating a Square instance with size as a tuple."""
        with self.assertRaises(TypeError):
            s1 = Square((1, 2, 3))

    def test_square_tuple_x(self):
        """Test creating a Square instance with x as a tuple."""
        with self.assertRaises(TypeError):
            s1 = Square(5, (1, 2, 3))

    def test_square_tuple_y(self):
        """Test creating a Square instance with y as a tuple."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, (1, 2, 3))

    def test_square_dict_size(self):
        """Test creating a Square instance with size as a dict."""
        with self.assertRaises(TypeError):
            s1 = Square({})

    def test_square_dict_x(self):
        """Test creating a Square instance with x as a dict."""
        with self.assertRaises(TypeError):
            s1 = Square(5, {})

    def test_square_dict_y(self):
        """Test creating a Square instance with y as a dict."""
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, {})

    def test_no_attr(self):
        """Test without attributes."""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_too_many_attr(self):
        """Test with too many attributes."""
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5, 6)


class TestSquareArea(unittest.TestCase):
    """Class that tests the area method."""

    def test_square_area(self):
        """Test the area method."""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_square_area_2(self):
        """Test the area method with all attributes set."""
        s1 = Square(3, 4, 5, 6)
        self.assertEqual(s1.area(), 9)


class TestSquareSetterGetter(unittest.TestCase):
    """Class that tests the setter and getter methods."""

    def test_square_getter(self):
        """Test the getter method of the class Square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_square_setter(self):
        """Test the setter method of the class Square."""
        s1 = Square(3)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_square_setter_string(self):
        """Test the setter method with a string."""
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.size = "hello"

    def test_square_setter_list(self):
        """Test the setter method with a list."""
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.size = [1, 2, 3]

    def test_square_setter_tuple(self):
        """Test the setter method with a tuple."""
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.size = (1, 2, 3)

    def test_square_setter_dict(self):
        """Test the setter method with a dictionary."""
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.size = {}

    def test_square_setter_float(self):
        """Test the setter method with a float."""
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.size = 5.1

    def test_square_setter_negative(self):
        """Test the setter method with a negative integer."""
        s1 = Square(3)
        with self.assertRaises(ValueError):
            s1.size = -5

    def test_square_setter_zero(self):
        """Test the setter method with a 0."""
        s1 = Square(3)
        with self.assertRaises(ValueError):
            s1.size = 0
