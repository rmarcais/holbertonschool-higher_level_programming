#!/usr/bin/python3
"""rectangle.py
Module that defines a class Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """Class called Rectangle that inherits from Base."""

    """The __init__ method is called when a new instance is created.
    Args:
    width: The width of the rectangle.
    height The height of the rectangle.
    x
    y
    id: public instance attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """public getter method."""
        return self.__width

    @width.setter
    def width(self, width):
        """public setter method."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """public getter method."""
        return self.__height

    @height.setter
    def height(self, height):
        """public setter method."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """public getter method."""
        return self.__x

    @x.setter
    def x(self, x):
        """public setter method."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """public getter method."""
        return self.__y

    @y.setter
    def y(self, y):
        """public setter method."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Method that prints in stdout the Rectangle instance with
        the character '#'.
        """
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Tells the main program how to print a Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute or that assigns
        a key/value argument to attributes."""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        else:
            my_list = ["id", "width", "height",
                       "x", "y"]
            i = 0
            for arg in args:
                setattr(self, my_list[i], arg)
                i += 1

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
