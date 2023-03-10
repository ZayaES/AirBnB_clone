#!/usr/bin/python3
# Written by Zaya Bell"

"""Defines a Rectangle class
This class can specify the height and width of a rectangle

"""


class Rectangle:
    """Defines a rectangle with optional width and height


    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of an instance rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of an instance rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(0, self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect = rect + ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
