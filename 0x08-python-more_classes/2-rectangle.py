#!/usr/bin/python3

""" A class that defines a rectangle """
class Rectangle:
    """ This represents a rectangle """
    def __init__(self, width = 0, height = 0):
        """ Initialization of rectangle class with :-
        args:
        * width - width of the rectangle
        * height - height of the rectangle
        raises:
        * TypeError - if size is not integer
        * ValueError - if size is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrives width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width attribute """
        if not isinstance(value, int):
            raise TypeError("Width must be integer")
        if value < 0:
            raise ValueError("Value can not be negative")
        self.__width = value

    @property
    def height(self):
        """ Retrives height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attribute """
        if not isinstance(value, int):
            raise TypeError("Height must be integer")
        if value < 0:
            raise ValueError("Height can not be negative")

        self.__height = value


    def area(self):
        """ Returns area of the rectangle """
        return (self.__width * self.__height)


    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

