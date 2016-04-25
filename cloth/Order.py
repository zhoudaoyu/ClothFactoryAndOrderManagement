#!/usr/bin/env python

__metaclass__ = type

class Order:
	def __init__(self, client_id, order_num):
		self.client_id = client_id
		self.order_num = order_num
		self.order_item_lst = list()
	
	def setOrderNum(self, order_num):
		self.order_num = order_num
	
	def getOrderNum(self):
		return self.order_num
		
	def setOrderItemList(self, order_item_lst):
		self.order_item_lst = order_item_lst
		
	def getOrderItemList(self):
		return self.order_item_lst

	def addOrderItem(self, order_item):
		self.order_item_lst.append(order_item)
		
	def removeOrderItem(self, order_item):
		self.order_item_lst.remove(order_item)
