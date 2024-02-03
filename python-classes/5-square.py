#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with a size attribute"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """Property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set it"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("Size must be >= 0")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints the square with the char #"""
        if self.__size > 0:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
