#!/usr/bin/python3.3

from classperson import Person
from random import randint
from display import *

def event(p1, p2):
	action = int(input('Действие: '))

	if action == 1:
		p1.punch(p2)
	elif action == 2:
		p1.kick(p2)
	elif action == 3:
		action = p1.block()

	return action
	
def event_2(p2, p1):
	action = randint(1, 3)

	if action == 1:
		p2.punch(p1)
	elif action == 2:
		p2.kick(p1)
	elif action == 3:
		action = p2.block()

	return action

p1 = Person('John', 10, 70, 2, 3, 10)
p2 = Person('Bot', 10, 70, 2, 3, 10)

while True:
	display(p1, p2)
	
	print('Выберите действие: 1 - удар рукой, 2 - удар ногой, 3 - блок')
	life_p1 = p1.health
	life_p2 = p2.health	

	act_p1 = event(p1, p2)
	act_p2 = event_2(p2, p1)

	if act_p1 == 3:
		p1.health = life_p1

	if act_p2 == 3:
		p2.health = life_p2