from random import randint
from art import *
from os import _exit, system
from time import sleep

def event(p1, p2):
	while True:
		action = input('Действие: ')

		if action.isdigit():
			action = int(action)

			if action == 1:
				p1.punch(p2)
			elif action == 2:
				p1.kick(p2)
			elif action == 3:
				action = p1.block()
			else:
				p1.wait()

			return action

		elif action == 'q':
			_exit(0)

		else:
			print('Внимательнее нужно быть!!! Попробуй еще раз')

	
def event_2(p2, p1):
	action = randint(1, 4)

	if action == 1:
		p2.punch(p1)
	elif action == 2:
		p2.kick(p1)
	elif action == 3:
		action = p2.block()
	else:
		p2.wait()

	return action

def match(p1, p2):
	if p1.health == 0 or p2.health == 0:
		sleep(2)
		system('clear')
		string_win = 'You are win!!!!!!'
		string_death = 'You are died!!!!!'
		if p1.health == 0 and p2.health == 0:
			print(string_death, ' ' * 44, string_death)
			print(person_death_death)
		elif p1.health == 0:
			print(string_death, ' ' * 44, string_win)
			print(person_death_win, end = '')
		else:
			print(string_win, ' ' * 44, string_death)
			print(person_win_death)
		_exit(0)
