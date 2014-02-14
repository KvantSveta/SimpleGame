from random import random
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
		if self.endurance - 3 >= 0:
			self.endurance -= 3
			if random() < self.precision + 0.1:
				#print('Удар рукой прошел', end = '')
				enemy.health -= self.hand
				if enemy.health < 0:
					enemy.health = 0
			return 1
		else:
			#print('Действие совершить нельзя', end = '')
			self.endurance += 2	
			return 4
	
	def kick(self, enemy):
		if self.endurance - 4 >= 0:
			self.endurance -= 4		
			if random() < self.precision - 0.2:
				#print('Удар ногой прошел', end = '')
				enemy.health -= self.leg
				if enemy.health < 0:
					enemy.health = 0
			return 2
		else:
			#print('Действие совершить нельзя', end = '')
			self.endurance += 2
			return 4

	def block(self):
		self.endurance += 1
		if random() < self.precision + 0.2:
			#print('Блок прошел', end = '')
			return 3
		return 0

	def wait(self):
		self.endurance += 2	
		return 4
