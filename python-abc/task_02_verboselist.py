#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """Class that inherits from the built-in list class"""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, new_items):
        super().extend(new_items)
        print("Extended the list with [{}] items.".format(len(new_items)))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed [{}] from the list.".format(item))
        except ValueError:
            print("{} is not in the list".format(item))

    def pop(self, index=-1):
        try:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
            return item
        except IndexError:
            print("Index {} doesn't exist".format(index))
