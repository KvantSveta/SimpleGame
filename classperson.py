from random import random

class Person():
	def __init__(self, health, precision, hand, leg):
		self.health = health
		self.precision = precision
		self.hand = hand
		self.leg = leg

	def punch(self):
		if random() < precision + 0.1:
			self.health -= hand
	
	def kick(self):		
		if random() < precision:
			self.health -= leg

	def display(self):
		print('Health    [' , self.health   , ' ]')
		print('Precision [' , self.precision, '%]')
		print('Punch     [ ', self.hand     , ' ]')
		print('Kick      [ ', self.leg      , ' ]')

p1 = Person(10, 70, 4, 6)
p2 = Person(10, 70, 4, 6)
p1.display()

