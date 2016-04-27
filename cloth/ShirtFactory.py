#!/usr/bin/env python

__metaclass__ = type

from ClothFactory import ClothFactory
from Shirt import Shirt
from time import sleep

class ShirtFactory(ClothFactory):
    def produce(self, shirt, quantity):
		print "It's producing shirts..."
		print '''The shirt attributes is: 
	STYLE 	 : %s
	SIZE  	 : %s
	COLOR 	 : %s
	ZIP TYPE : %s
					''' % (shirt.getStyle(), shirt.getSize(), shirt.getColor(), shirt.getZipType())
		print "Start to produce..."
		while True:
			if quantity == 0:
				print "Production completes!"
				break
			else:
				quantity = quantity - 1
				sleep(1)
				print "Quantity %i left." %  quantity
				
			
if __name__ == '__main__':
    pass