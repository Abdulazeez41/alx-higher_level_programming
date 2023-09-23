#!/usr/bin/python3
"""Define Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Module Representation of Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """module Square getters"""
        return self.width

    @size.setter
    def size(self, value):
        """module Square setters"""
        self.width = value
        self.height = value

    def __str__(self):
        """module string represation of square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
