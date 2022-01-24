#!/usr/bin/python3
"""8-rectangle.py
Write an empty class Rectangle that defines a rectangle
Private instance attribute: width:
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
. width must be an integer, otherwise raise a TypeError exception
 with the message width must be an integer
. if width is less than 0, raise a ValueError exception with
 the message width must be >= 0
Private instance attribute: height:
- property def height(self): to retrieve it
- property setter def height(self, value): to set it:
. height must be an integer, otherwise raise a TypeError
 exception with the message height must be an integer
. if height is less than 0, raise a ValueError
 exception with the message height must be >= 0
Public class attribute number_of_instances:
- Initialized to 0
- Incremented during each new instance instantiation
- Decremented during each instance deletion
Public class attribute print_symbol:
- Initialized to #
- Used as symbol for string representation
- Can be any type
Instantiation with optional width and height:
 def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self):
 that returns the rectangle perimeter:
. if width or height is equal to 0, perimeter is equal to 0
. repr() should return a string representation of the rectangle
 to be able to recreate a new instance by using eval()
. Print the message Bye rectangle... (... being 3 dots not ellipsis)
 when an instance of Rectangle is deleted
Static method def bigger_or_equal(rect_1, rect_2):
 that returns the biggest rectangle based on the area
- rect_1 must be an instance of Rectangle, otherwise raise a TypeError
 exception with the message rect_1 must be an instance of Rectangle
- rect_2 must be an instance of Rectangle, otherwise raise a TypeError
 exception with the message rect_2 must be an instance of Rectangle
- Returns rect_1 if both have the same area value
- Class method def square(cls, size=0):
 that returns a new Rectangle instance with width == height == size
"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    """Number of instances created"""

    print_symbol = "#"

    """The __init__  method is run as soon as the object class
    is instantiated.
    Args:
    width: The width of the rectangle
    height: The height of the rectangle
    __width: private instance attribute: The width of the rectangle
    __height: private instance attribute: the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property method
        Return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property method
        Args:
        value: The width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property method
        Return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property method
        Args:
        value: The height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method taht returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """This method tells the main program how to print a rectangle"""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i != self.__height - 1:
                    print()
        return ""

    def __repr__(self):
        """Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """This method prints the message Bye rectangle... (... being 3 dots
        not ellipsis) when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
