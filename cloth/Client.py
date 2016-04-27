#!/usr/bin/env python

__metaclass__ = type

from Order import Order
from OrderControlCenter import OrderControlCenter

class Client:
	def __init__(self, client_id):
		self.client_id = client_id
	
	#Create one order.
	def createOrder(self, order_num):
		self.order = Order(self.client_id, order_num)
		self.order.addOrderItem()
	
	def getOrder(self):
		return self.order
	
	def cacelOrder(self):
		del self.order
		
	def submitOrder(self):
		occ = OrderControlCenter()
		print "This order has been sent to order control center!"
		occ.patchOrder(self.order)
		
			
if __name__ == '__main__':
	client = Client(1)
	client.createOrder(10000)
	client.submitOrder()