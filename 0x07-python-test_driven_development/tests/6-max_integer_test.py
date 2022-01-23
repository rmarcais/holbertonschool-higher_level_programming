#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class to test the function def max_integer(list=[]):."""


    def test_max_ordered(self):
        """test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_unordered(self):
        """test with an unordered list"""
        self.assertEqual(max_integer([2, 8, 6, 10]), 10)

    def test_one_element(self):
        """test with a list of one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_negative_positive(self):
        """test with negative and positive numbers"""
        self.assertEqual(max_integer([-2, 3, -5, 8]), 8)

    def test_max_string(self):
        """test with a list of strings"""
        self.assertEqual(max_integer(["hello", "my", "school"]), "school")

    def test_max_tuple(self):
        """test with a list of tuples"""
        self.assertEqual(max_integer([(1, 2, 3), (52, 64, 87)]), (52, 64, 87))

    def test_max_float(self):
        """test with a list of floats"""
        self.assertEqual(max_integer([1.2, 5.6, 9.8, 7.1]), 9.8)

    def test_empty(self):
        """test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_int_float(self):
        """test with int and floats"""
        self.assertEqual(max_integer([1, 2.8, 5, 9.9]), 9.9)

    def test_isnone(self):
        """test when no list is passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_different_types(self):
        """test with different types"""
        with self.assertRaises(TypeError):
            max_integer([1, [2.1], 4])
        with self.assertRaises(TypeError):
            max_integer([1, (1, 2, 3), 4])
        with self.assertRaises(TypeError):
            max_integer(["hello", 2, "world !"])

    def test_integer(self):
        """test with an integer as list"""
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_string(self):
        """test with string as list"""
        self.assertEqual(max_integer(str(123)), '3')
        self.assertEqual(max_integer(str("hello")), "o")

if __name__ == '__main__':
    unittest.main()
