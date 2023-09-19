#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defining the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get private attrb"""
        return self.__width

    @property
    def height(self):
        """Get private attrb"""
        return self.__height

    @property
    def x(self):
        """Get private attrb"""
        return self.__x

    @property
    def y(self):
        """Get private attrb"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set private attrb"""
        self.setter_validation("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Set private attrb"""
        self.setter_validation("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Set private attrb"""
        self.setter_validation("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Set private attrb"""
        self.setter_validation("y", value)
        self.__y = value
