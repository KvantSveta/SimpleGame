#!/usr/bin/python3.3

from classperson import Person
from random import randint
from display import *
from time import sleep

os.system('clear')

def event(p1, p2):
	action = int(input('Действие: '))

	if action == 1:
		p1.punch(p2)
	elif action == 2:
		p1.kick(p2)
	elif action == 3:
		action = p1.block()
	elif action == 4:
		p1.wait()
	else:
		pass

	return action
	
def event_2(p2, p1):
	action = randint(1, 4)

	if action == 1:
		p2.punch(p1)
	elif action == 2:
		p2.kick(p1)
	elif action == 3:
		action = p2.block()
	elif action == 4:
		p2.wait()
	else:
		pass

	return action

p1 = Person('John', 1, 70, 3, 5, 13)
p2 = Person('Bot', 1, 70, 3, 5, 13)

display(p1, p2)

print(person_start)

while True:
	print('Выберите действие: 1 - удар рукой, 2 - удар ногой, 3 - блок, 4 - ожидать')
	
	life_p1 = p1.health
	life_p2 = p2.health	

	act_p1 = event(p1, p2)
	act_p2 = event_2(p2, p1)

	if act_p1 == 3:
		p1.health = life_p1
		
	if act_p2 == 3:
		p2.health = life_p2

	os.system('clear')
	
	display(p1, p2)

	if act_p1 == 1 and act_p2 == 1:
		print(person_punch_punch)
	elif act_p1 == 1 and act_p2 == 2:
		print(person_punch_kick)	
	elif act_p1 == 1 and act_p2 == 3:
		print(person_punch_block)
	elif act_p1 == 1 and act_p2 == 4:
		print(person_punch_wait)

	elif act_p1 == 2 and act_p2 == 1:
		print(person_kick_punch)
	elif act_p1 == 2 and act_p2 == 2:
		print(person_kick_kick)
	elif act_p1 == 2 and act_p2 == 3:
		print(person_kick_block)
	elif act_p1 == 2 and act_p2 == 4:
		print(person_kick_wait)

	elif act_p1 == 3 and act_p2 == 1:
		print(person_block_punch)
	elif act_p1 == 3 and act_p2 == 2:
		print(person_block_kick)
	elif act_p1 == 3 and act_p2 == 3:
		print(person_block_block)
	elif act_p1 == 3 and act_p2 == 4:
		print(person_block_wait)

	elif act_p1 == 4 and act_p2 == 1:
		print(person_wait_punch)
	elif act_p1 == 4 and act_p2 == 2:
		print(person_wait_kick)
	elif act_p1 == 4 and act_p2 == 3:
		print(person_wait_block)
	elif act_p1 == 4 and act_p2 == 4:
		print(person_wait_wait)

	else:
		print(person_start)

