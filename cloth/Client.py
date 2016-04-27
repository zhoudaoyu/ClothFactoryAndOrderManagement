#!/usr/bin/env python

__metaclass__ = type

from Order import Order


class Client:
	def __init__(self, client_id):
		self.client_id = client_id
	
	#Create one order.
	def createOrder(self, order_num):
		self.order = Order(self.client_id, order_num)
		while True:
			addOrderItemOrNote = raw_input("Do you want to add Item?(Y/N)")
			if addOrderItemOrNote == 'N':
				break
			elif addOrderItemOrNote == 'Y':
				self.order.addOrderItem()
			else:
				print "Please enter correct choose."
				continue
	
	def getOrder(self):
		return self.order
	
	def cacelOrder(self):
		del self.order
		
	def submitOrder(self):
		print "This order has been sent to order control center!"
			