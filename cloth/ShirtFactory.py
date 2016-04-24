#!/usr/bin/env python

__metaclass__ = type

from ClothFactory import ClothFactory
from Shirt import Shirt

class ShirtFactory(ClothFactory):
    def produce(self):
        shirt = Shirt('Man', 8, 'White', 'Snaps')
        print "It's producing shirts..."

if __name__ == '__main__':
    sf = ShirtFactory()
    sf.produce()
