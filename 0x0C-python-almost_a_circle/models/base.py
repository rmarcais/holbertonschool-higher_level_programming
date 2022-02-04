#!/usr/bin/python3
"""base.py
Module containing a class Base.
"""


import json


class Base:
    """The class Base is the 'base' of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs).
    __nb_objects: private class attribute.
    """
    __nb_objects = 0

    """The __init__ method is called when a new instance is created.
    Args:
    id: (always an integer) public instance attribute.
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        list_objs.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(cls.to_json_string(None))
            else:
                my_list = []
                for i in range(len(list_objs)):
                    my_list.append(list_objs[i].to_dictionary())
                f.write(cls.to_json_string(my_list))
