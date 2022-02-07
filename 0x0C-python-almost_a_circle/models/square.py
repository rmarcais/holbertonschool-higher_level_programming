#!/usr/bin/python3
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

    @property
    def size(self):
        """getter method"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute or that assigns
        a key/value argument to attributes."""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        else:
            my_list = ["id", "size",
                       "x", "y"]
            i = 0
            for arg in args:
                if i != 5:
                    setattr(self, my_list[i], arg)
                i += 1

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
