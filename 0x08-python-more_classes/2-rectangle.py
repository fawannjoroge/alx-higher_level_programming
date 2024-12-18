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
        return (self.__width * 2) + (self.__height*2)

