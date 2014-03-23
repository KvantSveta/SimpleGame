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
		if self.endurance >= 3:
			self.endurance -= 3
			if random() < self.precision_punch:
				print('Удар рукой выполнен!')
				enemy.health -= self.hand
				if enemy.health < 0:
					enemy.health = 0
			else:
				print('Удар рукой не выполнен! Промах!!')
			return 1
		else:
			print('Для действия не хватает энергии')
			self.endurance = 13
			return 4

	def kick(self, enemy):
		if self.endurance  >= 4:
			self.endurance -= 4
			if random() < self.precision_kick:
				print('Удар ногой выполнен!')
				enemy.health -= self.leg
				if enemy.health < 0:
					enemy.health = 0
			else:
				print('Удар ногой не выполнен! Промах!!!')
			return 2
		else:
			print('Для действия не хватает энергии')
			self.endurance = 13
			return 4

	def block(self):
		if self.endurance < 13:
			self.endurance += 1
		if random() < self.precision_block:
			print('Блок выполнен!')
			return 3
		else:
			print('Блок не выполнен!')
			return 0

	def wait(self):
		print('Ожидание!')
		self.endurance = 13
		return 4
