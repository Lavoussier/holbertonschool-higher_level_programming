#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with a size attribute"""

    def __init__(self, side_length=0):
        """Instantiation with optional side length"""
        self.__side_length = side_length

    @property
    def side_length(self):
        """Property to retrieve it"""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """Property setter to set it"""
        if not isinstance(value, int):
            raise TypeError("Side length must be an integer")
        if value >= 0:
            self.__side_length = value
        else:
            raise ValueError("Side length must be >= 0")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.side_length ** 2
