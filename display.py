from art import *
import os

def	display(p1, p2):
	length = 9
	tab = '                                            '
	print('Name'.ljust(length), p1.name.ljust(7), tab, 'Name'.ljust(length), p2.name.ljust(7))
	print('Health'.ljust(length), '[', str(p1.health).rjust(2), ' ]', tab ,'Health'.ljust(length), '[', str(p2.health).rjust(2), ' ]')
	print('Precision'.ljust(length), '[', p1.precision, '%]', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
	print('Punch'.ljust(length), '[ ', p1.hand, ' ]', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
	print('Kick'.ljust(length), '[ ', p1.leg, ' ]', tab, 'Kick'.ljust(length), '[ ', p2.leg, ' ]')
	print('Endurance'.ljust(length), '[', str(p1.endurance).rjust(2), ' ]', tab, 'Endurance'.ljust(length), '[', str(p2.endurance).rjust(2), ' ]')
	if p1.is_dead() or p2.is_dead():
		string = 'You are died!!!!!'
		if p1.is_dead() and p2.is_dead():
			print(string, ' ' * 44 , string, end = '')
			print(person_death_death)
		elif p1.is_dead():
			print(string, end = '')
			print(person_death_win, end = '')
		#print(tab, end = '')
		else:
			print(' ' * 62, string, end = '')
			print(person_win_death)
		os._exit(0)