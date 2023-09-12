#!/usr/bin/python3
'''
Geometry | Rectangle class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle
    '''
    def __init__(self, width, height):
    '''
        Constructor to assign width and height at runtime

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
