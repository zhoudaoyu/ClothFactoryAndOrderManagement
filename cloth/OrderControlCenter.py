#!/usr/bin/env python

__metaclass__ = type

class OrderControlCenter:
	def patchOrder(self, order):
		for order_item in order.order_item_lst:
			if order_item.cloth_type == 'Shirt':
				from ShirtFactory import ShirtFactory
				factory = ShirtFactory()
		
			factory.produce(order_item.cloth, order_item.quantity)