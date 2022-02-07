#!/usr/bin/python3
"""base.py
Module containing a class Base.
"""


import json
import os
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string representaion
        (json_string).
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes
        already set.
        Args:
        **dictionary: The dictionary representation of an instance.
        """
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances."""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, "r") as f:
                my_list = cls.from_json_string(f.read())
                list_ins = []
                for i in range(len(my_list)):
                    dummy = cls.create(**my_list[i])
                    list_ins.append(dummy)
                return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method that opens a window and draws all
        the Rectangles and Squares.
        Args:
        list_rectangles: A list of Rectangle instances.
        list_squares: A list of Squares instances.
        """
        turtle.color("green")
        turtle.shape("turtle")
        turtle.pencolor("green")
        turtle.speed(3)
        turtle.pensize(5)
        for rectangles in list_rectangles:
            turtle.penup()
            turtle.goto(rectangles.x, rectangles.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rectangles.width)
                turtle.right(90)
                turtle.forward(rectangles.height)
                turtle.right(90)

        for squares in list_squares:
            turtle.penup()
            turtle.goto(squares.x, squares.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(squares.size)
                turtle.right(90)
                turtle.forward(squares.size)
                turtle.right(90)

        turtle.penup()
        turtle.goto(-200, -200)
        turtle.write("Done ! (click to exit)", font=("Arial", 16, "normal"))
        turtle.hideturtle()
        turtle.exitonclick()
