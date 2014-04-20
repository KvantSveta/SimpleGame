from random import random

class Person:
	def __init__(self, name, health, precision, hand, leg, endurance):
		self.name = name
		self.health = health
		self.precision = precision
		self.precision_punch = precision + 0.1
		self.precision_kick = precision - 0.1
		self.precision_block = precision + 0.2
		self.hand = hand
		self.leg = leg
		self.endurance = endurance

	def punch(self, enemy):
		self.endurance -= 3
		if random() < self.precision_punch:
			enemy.health -= self.hand
			if enemy.health < 0:
				enemy.health = 0
		return 1

	def kick(self, enemy):
		self.endurance -= 4
		if random() < self.precision_kick:
			enemy.health -= self.leg
			if enemy.health < 0:
				enemy.health = 0
		return 2

	def block(self):
		if self.endurance < 13:
			self.endurance += 1
		if random() < self.precision_block:
			return 3
		else:
			return 0

	def wait(self):
		self.endurance = 13
		return 4
