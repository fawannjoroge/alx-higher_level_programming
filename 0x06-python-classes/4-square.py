#!/usr/bin/python3
class Square:
    def __init__(self,size=0):
        self.size = size
    def area(self):
        return (self.__size)**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,value):
        if type(value) is not int:
            raise TypeError('value must be an integer')
        else:
            if value < 0:
                raise ValueError('value must be >= 0')
            else:
                self.__size = value

        
