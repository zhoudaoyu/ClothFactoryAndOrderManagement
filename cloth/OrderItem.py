#!/usr/bin/env python

__metaclass__ = type

from Shirt import Shirt

class OrderItem:
	def __init__(self, order_item_num, cloth_type = '', quantity = 1):
		self.order_item_num = order_item_num
		self.cloth_type = cloth_type
		self.quantity = quantity
		self.cloth = None

	def setClothType(self, cloth_type):
		self.cloth_type = cloth_type
		if cloth_type == 'Shirt':
			style = raw_input("Do you want to buy %s for Man or Woman? (M/W): " % self.cloth_type)
			size = raw_input("Please provide the size: ")
			color = raw_input("Please provide the color you want: ")
			zip_type = raw_input("Please provide the zip type you want: ")
			self.setCloth(Shirt(style, size, color, zip_type))	
			
			
	def getClothType(self):
		return cloth_type
		
	def setQuantity(self, quantity):
		self.quantity = quantity
	
	def getQuantity(self):
		return quantity		
	
	def setCloth(self, cloth):
		self.cloth = cloth
	
	def getCloth(self):
		return self.cloth