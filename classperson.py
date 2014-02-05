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
			if enemy.health < 0:
				enemy.health = 0
	
	def kick(self, enemy):		
		if random() < self.precision - 0.17:
			enemy.health -= self.leg
			if enemy.health < 0:
				enemy.health = 0

	def block(self, enemy):
		if random() > self.precision + 0.2:
			if enemy.punch():
				pass

	def is_dead(self):
		if self.health == 0:
			print('You are died', end = '')


