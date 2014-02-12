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
				#print('Удар рукой прошел')
				enemy.health -= self.hand
				if enemy.health < 0:
					enemy.health = 0
		else:
			print('Действие совершить нельзя')
			self.endurance += 2	
	
	def kick(self, enemy):
		if self.endurance - 4 >= 0:
			self.endurance -= 4		
			if random() < self.precision - 0.2:
				#print('Удар ногой прошел')
				enemy.health -= self.leg
				if enemy.health < 0:
					enemy.health = 0
		else:
			print('Действие совершить нельзя')
			self.endurance += 2

	def block(self):
		self.endurance += 1
		if random() < self.precision + 0.2:
			print('Блок прошел')
			return 3
		return 0

	def is_dead(self):
		if self.health == 0:
			return True


