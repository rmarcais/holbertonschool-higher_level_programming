#!/usr/bin/python3
"""100-my_int.py
The class MyInt is a rebel. MyInt has == and != operators inverted.
You are not allowed to import any module.
"""


class MyInt(int):
    """class that inherits from int."""

    """__init__ method that is called when a new instnace is created."""
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Tests if an integer is equal to another integer.
        It returns False if yes, True otherwise.
        """
        return self.value != other

    def __ne__(self, other):
        """Tests if an integer is not equal to another integer.
        It returns False if yes, True otherwise.
        """
        return self.value == other
