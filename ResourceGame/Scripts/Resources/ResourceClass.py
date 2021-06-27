###### RESOURCE CLASS FILE ######

#### Imports ####
import pygame

#### Producer class ####
class Producer:
	def __init__(self, loc, img, amount):
		self.loc = loc
		self.img = img
		self.amount = amount
		self.resource = 0

	def collect(self):
		self.resource += self.amount

#### Collector class ####
class Collector:
	def __init__(self):
		self.amount = 0
		self.prod_list = []

	def collect(self):
		for prod in self.prod_list:
			prod.collect()
			self.amount += prod.resource
			prod.resource = 0