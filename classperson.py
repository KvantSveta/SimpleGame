from random import randint
from os import _exit

class Person:
	def __init__(self, name, health, precision, hand, leg, endurance):
		self.name = name
		self.health = health
		self.precision = precision
		self.hand = hand
		self.leg = leg
		self.endurance = endurance

	def punch(self, enemy):
		self.endurance -= 2
		if randint(1, 100) < self.precision + 10:
			enemy.health -= self.hand
			if enemy.health < 0:
				enemy.health = 0
	
	def kick(self, enemy):
		self.endurance -= 3		
		if randint(1, 100) < self.precision - 17:
			enemy.health -= self.leg
			if enemy.health < 0:
				enemy.health = 0

	def block(self):
		self.endurance += 1
		if randint(1, 100) > self.precision + 20:
			pass

	def is_dead(self):
		if self.health == 0:
			print('You are died', end = '')
			_exit(0)


