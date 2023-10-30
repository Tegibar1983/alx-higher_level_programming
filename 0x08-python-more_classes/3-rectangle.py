#!/usr/bin/python3

""" A class that defines a rectangle """
class Rectangle:
    """ This represents rectangle"""
    def __init__(self, width = 0, height = 0):
        """ Initializing this rectangle class with :-
        args:
        * width - width of the rectangle
        * height - height the rectangle
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
        if not isinstance(value, int):
            raise TypeError("Width must be integer")
        if value < 0:
            raise ValueError("Width can not be negative")

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
            raise ValueError("Height must be positive value")

        self.__height = value


    def area(self):
        """ Returns the area of this rectangle """
        return (self.__width * self.__height)


    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))


    def __str__(self) -> str:
        """ Presents diagram of the defined rectangle object """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for raw in range(self.__width):
                rectangle += "#"
        if column < self.__height - 1:
            rectangle += "\n"
        return (rectangle)

