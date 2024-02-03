#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with the char #"""
        if self.__size == 0:
            print("")
            return
        rows, cols = self.__position[1], self.__position[0]
        print("\n" * rows, end="")
        for _ in range(self.__size):
            print(" " * cols + "#" * self.__size)
