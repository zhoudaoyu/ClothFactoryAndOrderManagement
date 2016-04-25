#!/usr/bin/env python

__metaclass__ = type

from Order import Order
from OrderItem import OrderItem

class Client:
	def __init__(self, client_id):
		self.client_id = client_id
	
	#Create one order.
	def createOrder(self, order_num):
		self.order = Order(self.client_id, order_num)
		# while True:
			# addOrderItemOrNote = raw_input("Do you want to add Item?(Y/N)")
			# if addOrderItemOrNote == 'N':
				# break
			# elif addOrderItemOrNote == 'Y':
				# self.createOrderItem(order_item_num)
			# else:
				# print "Please enter correct choose."
				# continue
	
	def cacelOrder(self):
		pass
		
	#Create one order item.
	def createOrderItem(self, order_item_num):
		order_item = OrderItem(order_item_num)
		cloth_type = raw_input("Please choose the cloth type you want to buy: ")
		quantity = int(raw_input("Please choose the cloth type you want to buy: "))
		order_item.setClothType(order_item)
		order_item.setQuantity(quantity)
		#Add this order item to order
		self.order.addOrderItem(order_item)

	def removeOrderItem(self, order_item_num):
		for order_item in self.order: 
			if order_item.count(order_item_num) != 0:
				self.order.removeOrderItem(order_item)
		
	def submitOrder(self):
		for order_item in self.order.getOrderItemList():
			