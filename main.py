#!/usr/bin/python3.3

from classperson import Person
from art import *

def	display(p1, p2):
	length = 9
	tab = '                                       '
	print('Name'.ljust(length), p1.name, '       ', tab, 'Name'.ljust(length), p2.name)
	print('Health'.ljust(length), '[', p1.health, ' ]', '    ', tab ,'Health'.ljust(length), '[', p2.health   , ' ]')
	print('Precision'.ljust(length), '[', p1.precision, '%]', '    ', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
	print('Punch'.ljust(length), '[ ', p1.hand, ' ]', '    ', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
	print('Kick'.ljust(length), '[ ', p1.leg, ' ]', '    ', tab, 'Kick'.ljust(length), '[ ', p1.leg, ' ]')
	print(person_new)

p1 = Person('John', 10, 70, 4, 6)
p2 = Person('Bot', 10, 70, 4, 6)

display(p1, p2)

p1.punch(p2)
