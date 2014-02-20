from random import randint

class Person:
	def __init__(self, name, health, precision, hand, leg, endurance):
		self.name = name
		self.health = health
		self.precision = precision
		self.precision_punch = precision + 10
		self.precision_kick = precision - 10
		self.precision_block = precision + 20
		self.hand = hand
		self.leg = leg
		self.endurance = endurance

	def punch(self, enemy):
		if self.endurance >= 3:
			self.endurance -= 3
			if randint(1, 100) < self.precision_punch:
				enemy.health -= self.hand
				if enemy.health < 0:
					enemy.health = 0
			return 1
		else:
			self.endurance += 5	
			return 4
	
	def kick(self, enemy):
		if self.endurance  >= 4:
			self.endurance -= 4		
			if randint(1, 100) < self.precision_kick:
				enemy.health -= self.leg
				if enemy.health < 0:
					enemy.health = 0
			return 2
		else:
			self.endurance += 5
			return 4

	def block(self):
		self.endurance += 1
		if randint(1, 100) < self.precision_block:
			return 0
		return 3

	def wait(self):
		self.endurance += 5	
		return 4
