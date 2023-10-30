#!/usr/bin/python3

""" A class that defines a Rectangle """
class Rectangle:
    """ This represents a rectangle """
    number_of_instances = 0

    def __init__(self, width, height):
        """ Initializing this rectangle class with:-
        args:
        * width - width of the rectangle
        * height - height of the rectangle
        raises:
        * TypeError - if size is not integer
        * ValueError - if size is not positive
        """

        self.width = width
        self.height = height


    @property
    def width(self):
        """ Retrives width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width attributes """
        if not isinstance(value, int):
            raise TypeError("Width must be integer")
        if value < 0:
            raise ValueError("Width must be positive")

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
            raise ValueError("Height must be positive")

        self.__height = value

    def area(self):
        """ Returns area of the rectangle """
        return (self.__width * self.__height)


    def perimeter(self):
        """ Returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ Presents diagram of rectangle object """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""

        if column in range(self.__height):
            if raw in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)


    def __repr__(self):
        """ Returns string representaion of a rectangle """
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)


    def __del__(self):
        """ prints deleted mesaage for rectangle object """
        print("Bye Rectangle ...")
        Rectangle.number_of_instances -= 1






