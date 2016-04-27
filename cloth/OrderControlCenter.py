#!/usr/bin/env python

__metaclass__ = type

class OrderControlCenter:
	def patchOrder(self, order):
		for order_item in order:
			if order_item.cloth_type == 'Shirt':
				from ShirtFactory import ShirtFactory
				factory = ShirtFactory()
		
			factory.product(order_item.cloth, order_item.quantity)