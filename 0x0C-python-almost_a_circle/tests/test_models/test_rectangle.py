#!/usr/bin/python3
"""
Add unit test for the class Rectangle.
"""
import sys
import io
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Area(unittest.TestCase):

    def test_area(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """
        p1 = Rectangle(2, 3)
        self.assertEqual(p1.area(), 6)

    def test_area_neg(self):
        """Test with height and width less than 0."""
        with self.assertRaises(ValueError):
            p1 = Rectangle(-5, -5)
            p1.area()

    def test_area_zero(self):
        """Test with width and width equal to 0."""
        with self.assertRaises(ValueError):
            p1 = Rectangle(0, 0)
            p1.area()

    def test_area_bool(self):
        """Test the area method with boolean values."""
        with self.assertRaises(TypeError):
            r = Rectangle(True, True)
            r.area()

    def test_area_str(self):
        """Test the area method with strings."""
        with self.assertRaises(TypeError):
            r = Rectangle("Alfred", "Robin")
            r.area()

    def test_area_tuple(self):
        """Test the area method with tuples"""
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2, 3), (1, 2, 3))
            r.area()

    def test_area_list(self):
        """Test the area method with lists."""
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2, 3], [1, 2, 3])
            r.area()

    def test_area_dict(self):
        """Test the area method with dictionaries."""
        with self.assertRaises(TypeError):
            r = Rectangle({1, 2, 3}, {1, 2, 3})
            r.area()

    def test_area_float(self):
        """Test the area method with floats."""
        with self.assertRaises(TypeError):
            r = Rectangle(float("inf"), 7)
            r.area()
        with self.assertRaises(TypeError):
            r = Rectangle(float("NaN"), 7)
            r.area()

    def test_area_empty(self):
        """Test area() whitout attributes."""
        with self.assertRaises(TypeError):
            r = Rectangle()
            r.area()

    def test_area_None(self):
        """Test area() with None."""
        with self.assertRaises(TypeError):
            r = Rectangle(None, None)
            r.area()


class Test_display(unittest.TestCase):

    def test_display(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """

        r = Rectangle(2, 2, 3, 4)
        self.assertEqual(r.display(), None)

    def test_display_neg(self):
        """Test the display method with negatives values."""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, -5, -5, -5)
            r.display()

    def test_display_zero(self):
        """Test the display method with 0."""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0, 0, 0)
            r.display()

    def test_display_bool(self):
        """Test the display method with bool values."""
        with self.assertRaises(TypeError):
            r = Rectangle(True, False, False, True)
            r.display()

    def test_display_str(self):
        """Test the display method with strings."""
        with self.assertRaises(TypeError):
            r = Rectangle("Alfred", "Robin", "Batman", "Batgirl")
            r.display()

    def test_display_tuple(self):
        """Test the display method with tuples."""
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3))
            r.display()

    def test_display_list(self):
        """Test the display method with lists."""
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
            r.display()

    def test_display_dict(self):
        """Test the display method with dictionaries."""
        with self.assertRaises(TypeError):
            r = Rectangle({1, 2, 3}, {1, 2, 3},
                          {1, 2, 3}, {1, 2, 3})
            r.display()

    def test_display_float_inf(self):
        """Test the display method with float inf."""
        with self.assertRaises(TypeError):
            r = Rectangle(float("inf"), float("inf"),
                          float("inf"), float("inf"))
            r.display()

    def test_display_float_NaN(self):
        """Test the display method with float NaN."""
        with self.assertRaises(TypeError):
            r = Rectangle(float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
            r.display()

    def test_display_empty(self):
        """Test the display method without arguments."""
        with self.assertRaises(TypeError):
            r = Rectangle()
            r.display()

    def test_display_None(self):
        """Test the display method with None."""
        with self.assertRaises(TypeError):
            r = Rectangle(None, None, None, None)
            r.display()


class Test_width(unittest.TestCase):

    def test_width(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """
        r = Rectangle(5, 5, 2, 3)
        self.assertEqual(r.width, 5)

    def test_width_neg(self):
        """Test with negative width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(ValueError):
            r.width = -6

    def test_width_zero(self):
        r = Rectangle(1, 1, 1, 1, 1)
        """Test with width equal to 0."""
        with self.assertRaises(ValueError):
            r.width = 0

    def test_width_bool(self):
        """Test with bool width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = True

    def test_width_str(self):
        """Test with string width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = "hello"

    def test_width_tuple(self):
        """Test with tuple width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = (1, 2, 3)

    def test_width_list(self):
        """Test with list width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = [1, 2, 3]

    def test_width_dict(self):
        """Test with dict width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = {}

    def test_width_float_inf(self):
        """Test with float width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = 1.1

    def test_width_float_NaN(self):
        """Test with float NaN width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = float("NaN")

    def test_width_empty(self):
        """Test with empty width."""
        with self.assertRaises(TypeError):
            r = Rectangle()
            r.width()

    def test_width_None(self):
        """Test with None width."""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.width = None


class Test_height(unittest.TestCase):

    def test_height(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """
        r = Rectangle(5, 5, 2, 3)
        self.assertEqual(r.height, 5)

    def test_height_neg(self):
        """Test with negative hight."""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, -5, -5, -5)
            r.height()

    def test_height_zero(self):
        """Test with 0 hight."""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 0, -5, -5)
            r.height()

    def test_height_bool(self):
        """Test with bool hight."""
        with self.assertRaises(TypeError):
            r = Rectangle(True, False, False, True)
            r.height()

    def test_height_str(self):
        """Test with string hight."""
        with self.assertRaises(TypeError):
            r = Rectangle("Alfred", "Robin", "Batman", "Batgirl")
            r.height()

    def test_height_tuple(self):
        """Test with tuple hight."""
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3))
            r.height()

    def test_height_list(self):
        """Test with list hight."""
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
            r.height()

    def test_height_dict(self):
        """Test with dict hight."""
        with self.assertRaises(TypeError):
            r = Rectangle({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3})
            r.height()

    def test_height_float_inf(self):
        """Test with float hight."""
        with self.assertRaises(TypeError):
            r = Rectangle(float("inf"), float("inf"),
                          float("inf"), float("inf"))
            r.height()

    def test_height_flaot_NaN(self):
        """Test with float NaN hight."""
        with self.assertRaises(TypeError):
            r = Rectangle(float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
            r.height()

    def test_height_empty(self):
        """Test with empty hight."""
        with self.assertRaises(TypeError):
            r = Rectangle()
            r.height()

    def test_height_None(self):
        with self.assertRaises(TypeError):
            r = Rectangle(None, None, None, None)
            r.height()


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the Rectangle Class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(2, Rectangle(10, 8, 6, 4, 2).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 0, 0, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 0, 0, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 0, 0, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 0, 0, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 1, 0, 1)
        self.assertEqual(1, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 1, 0, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 0, 1, 1)
        self.assertEqual(1, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 0, 1, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_x(unittest.TestCase):
    """Unittests for Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for __str__ method of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        r = Rectangle(3, 4)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = f"[Rectangle] ({r.id}) 0/0 - 3/4\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(3, 4, 1)
        correct = f"[Rectangle] ({r.id}) 1/0 - 3/4"
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(3, 4, 1, 2)
        correct = f"[Rectangle] ({r.id}) 1/2 - 3/4"
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(3, 4, 1, 2, 9)
        self.assertEqual("[Rectangle] (9) 1/2 - 3/4", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(1, 2, 3, 4, 7)
        r.width = 15
        r.height = 12
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] (7) 8/10 - 15/12", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for update args method of the Rectangle class."""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = f"[Rectangle] ({r.id}) 2/10 - 4/5"
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        r.update(6, 5, 4, 3, 2)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = f"[Rectangle] ({r.id}) 10/9 - 10/7"
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
