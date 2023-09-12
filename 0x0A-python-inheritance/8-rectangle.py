#!/usr/bin/python3
'''
    Implementing a Geometry class using Rectangle class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle
    '''
    def __init__(self, width, height):
    '''
        Constructor to assign width and height at runtime
    '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
