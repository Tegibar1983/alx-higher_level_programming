#!/usr/bin/python3

""" A class that defines a rectangle """

class Rectangle:
    """ This represents a rectangle """

    def __init__(self, width, height):

    """ Initializing this  rectangle class with:-
    args:
    * Width - width of the rectangle
    * Height - height of the rectangle
    raises:
    * TypeError - Size must be integer
    * ValueError - Size must be positive
    """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrives width attribute """
        return self.__width

    @width.setter
    def width(self, value):
    """ Sets width of the rectangle """
    if not isinstance(value, int):
        raise TypeError("Width must be interger")
    if value < 0:
        raise ValueError("Width must be positive")
    self.__width = value

    @property
    def height(self):
        """ Retrives height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("Height must be integer")
        if value < 0:
            raise ValueError("Height must be positive")

        self.__height = value


    def area(self):
        """ Returns area of the rectangle """
        return (self.__width * self.__height)


    def perimeter(self):
        """ Returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ presents diameter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return = ("")
        rectangle = ""

        for column in range(self.__height):
            for raw in range(self.__width):
                rectangle += "#"

            if column < self.__height - 1:
                rectangle += "\n"

        return (rectangle)

    def __repr__(self):
        """ Return string representaion of rectangle """
        return "Rectangle ({:d}, {:d}".format(self.__width, self.__height))


    def __del__(self):
        """ Prints Removal message for every deleted object """
        print("Bye Rectangle ...")






