#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        print("__init__")
        self.size = size

    @property
    def size(self):
        # print("@size.getter")
        return self.__size

    @size.setter
    def size(self, value):
        # print("@size.setter")
        self.__size = value

    def __add__(self, variable):
        if type(variable) is int:
            self.size = self.size + variable
        else:
            print("Are you trying to make a rectangle ?")
        return self

    def my_print(self):
        for i in range(self.size):
            print('#' * self.size)

    def my_print(self, number=0):
        pass
