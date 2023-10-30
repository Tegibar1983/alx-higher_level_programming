#!/usr/bin/python3

""" A class that defines a class """
class Rectangle:
    """Rectangle representation """
    def __init__(self, width = 0, height = 0):
        """ initializing this Rectangle class:-
        args:
        * width - represents Rectangle width
        * height - represents Rectangle height
        raises:
        * TypeError - if size is non integer
        * ValueError _ if size is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrives width attribute """
        return self.__width
    @width.setter
    def width(self, value):
        """ sets width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
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
            raise ValueError("Value can not be negative")
        self.___height = value




