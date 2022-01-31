#!/usr/bin/python3
"""1-my_list.py
Test file: 1-my_list.txt
Class: MyList
Method(s): print_sorted
To test this method, run:
python3 -m doctest ./test/1-my_list.txt
"""


class MyList(list):
    """class that inherits from list."""
    def print_sorted(self):
        """prints the sorted list (ascending sort)."""
        print(sorted(self))
