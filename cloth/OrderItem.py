#!/usr/bin/env python

__metaclass__ = type

class OrderItem:
	def __init__(self):
		pass
		
	def setQuantity(self, order_item_num, cloth_type = '', quantity = 1):
		self.order_item_num = order_item_num
		self.cloth_type = cloth_type
		self.quantity = quantity

	def setClothType(self, cloth_type):
		self.cloth_type = cloth_type
	
	def getClothType(self)
		return cloth_type
		
	def setQuantity(self, setQuantity):
		self.quantity = quantity
	
	def getQuantity(self)
		return quantity		
	