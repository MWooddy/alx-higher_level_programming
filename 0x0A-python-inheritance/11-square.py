#!/usr/bin/python3
"""
Create a class Square that inherits from class: Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square - is a sub class of Rectangle."""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Overwrite the __str__ method of the parent class Rectangle."""
        return f"[Square] {self.__size}/{self.__size}"
