#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with a size attribute"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = self.__validate_and_set_size(size)

    def __validate_and_set_size(self, size):
        """Validate and set the size attribute"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        return size

    def area(self):
        """Public instance method to calculate the area"""
        return self.__size ** 2
