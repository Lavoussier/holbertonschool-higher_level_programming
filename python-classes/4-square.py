#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with a size attribute"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self._size = size

    @property
    def size(self):
        """Property to retrieve it"""
        return self._size

    @size.setter
    def size(self, value):
        """Property setter to set it"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self._size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.size ** 2
