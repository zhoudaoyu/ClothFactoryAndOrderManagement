#!/usr/bin/env python

__metaclass__ = type

from OrderItem import OrderItem



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

	def addOrderItem(self):
		order_item_num = 0
		while True:
			addOrderItemOrNot = raw_input("Do you want to add Item?(Y/N): ")
			print addOrderItemOrNot
			if addOrderItemOrNot == 'N':
				break
			elif addOrderItemOrNot == 'Y':
				order_item_num = order_item_num + 1
				order_item = OrderItem(order_item_num)
				cloth_type = raw_input("Please choose the cloth type you want to buy: ")
				quantity = int(raw_input("Please set the quantity you want to buy: "))
				order_item.setClothType(cloth_type)
				order_item.setQuantity(quantity)
				#Add this order item to order
				self.order_item_lst.append(order_item)
			else:
				print "Please enter correct choose."
				continue	
		
		
	def removeOrderItem(self, order_item):
		self.order_item_lst.remove(order_item)
		
	def listOrderItem(self):
		pass
