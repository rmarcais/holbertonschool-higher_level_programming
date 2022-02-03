#!/usr/bni/python3
"""square.py
Modules that defines a class Square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square."""

    """The __init__ method is called when a new intance is created."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method tells the main program how to print a square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
