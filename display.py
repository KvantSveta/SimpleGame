from art import *
import os

def	display(p1, p2):
	length = 9
	tab = '                                       '
	print('Name'.ljust(length), p1.name, '       ', tab, 'Name'.ljust(length), p2.name)
	print('Health'.ljust(length), '[', p1.health, ' ]', '    ', tab ,'Health'.ljust(length), '[', p2.health   , ' ]')
	print('Precision'.ljust(length), '[', p1.precision, '%]', '    ', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
	print('Punch'.ljust(length), '[ ', p1.hand, ' ]', '    ', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
	print('Kick'.ljust(length), '[ ', p1.leg, ' ]', '    ', tab, 'Kick'.ljust(length), '[ ', p2.leg, ' ]')
	print('Endurance'.ljust(length), '[', p1.endurance, ' ]', '    ', tab, 'Endurance'.ljust(length), '[', p2.endurance, ' ]')
	if p1.is_dead() or p2.is_dead():
		if p1.is_dead():
			print('You are died')
			print(person_death_win, end = '')
		print(tab, end = '')
		if p2.is_dead():
			print('You are died')
			print(person_win_death)
		os._exit(0)