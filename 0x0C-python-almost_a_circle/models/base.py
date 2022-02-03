#!/usr/bin/python3
"""base.py
Module containing a class Base.
"""


class Base:
    """The class Base is the 'base' of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs).
    """
    __nb_objects = 0

    """The __init__ method is called when a new instance is created."""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
