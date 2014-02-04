from random import random
from art import *

class Person():
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

def	display(p1, p2):
		#print((str(self.health)).ljust(9),'Health')
		length = 9
		tab = '\t\t\t\t\t'
		print('Name'.ljust(length), p1.name, '     ', tab, 'Name'.ljust(length), p2.name)
		print('Health'.ljust(length), '[', p1.health, ' ]', '   ', tab ,'Health'.ljust(length), '[', p2.health   , ' ]')
		print('Precision'.ljust(length), '[', p1.precision, '%]', '  ', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
		print('Punch'.ljust(length), '[ ', p1.hand, ' ]', '  ', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
		print('Kick'.ljust(length), '[ ', p1.leg, ' ]', '  ', tab, 'Kick'.ljust(length), '[ ', p1.leg, ' ]')

p1 = Person('John', 10, 70, 4, 6)
p2 = Person('Bot', 10, 70, 4, 6)

display(p1, p2)

p1.punch(p2)
