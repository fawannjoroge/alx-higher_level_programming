#!/usr/bin/python3
class Rectangle:
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height =value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        else:
            if value < 0:
                raise ValueError('height must be >= 0')
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height*2)

    def __str__(self):
        string =""
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join('#' * self.__width for j in range(self.__height))
        return string
