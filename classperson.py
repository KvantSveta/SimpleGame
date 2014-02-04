from random import random

class Person:
	def __init__(self, name, health, precision, hand, leg):
		self.name = name
		self.health = health
		self.precision = precision
		self.hand = hand
		self.leg = leg

	def punch(self, enemy):
		if random() < self.precision + 0.1:
			enemy.health -= self.hand
	
	def kick(self, enemy):		
		if random() < self.precision:
			enemy.health -= self.leg

