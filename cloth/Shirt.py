#!/usr/bin/env python

__metaclass__ = type

from Cloth import Cloth

class Shirt(Cloth):
    def __init__(self, style, size, color, zip_type):
        super(Shirt, self).__init__(style, size, color)
        self.zip_type = zip_type

    def setZipType(self, zip_type):
        self.zip_type = zip_type

    def getZipType(self):
        return self.zip_type

if __name__ == '__main__':
    shirt = Shirt('Man', 8, 'White', 'Snaps')
    print shirt.style
    print shirt.size
    print shirt.color
    print shirt.zip_type
