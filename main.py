#!/usr/bin/python3.3

from classperson import Person
from display import display
from event import *
from os import system

system('clear')

p1 = Person('John', 15, 70, 3, 5, 13)
p2 = Person('Bot', 15, 70, 3, 5, 13)

display(p1, p2)

print(person_start)

while True:
	print('1 - удар рукой({0}%), 2 - удар ногой({1}%), 3 - блок({2}%), 4 - ожидать, q - выйти'.format(p1.precision_punch, p1.precision_kick, p1.precision_block))
	
	life_p1 = p1.health
	life_p2 = p2.health	

	act_p1 = event(p1, p2)
	act_p2 = event_2(p2, p1)

	if act_p1 == 0:
		p1.health = life_p1
		act_p1 = 3
		
	if act_p2 == 0:
		p2.health = life_p2
		act_p2 = 3

	system('clear')
	
	display(p1, p2)

	for i in range(1, 5):
		for j in range(1, 5):
			if act_p1 == i and act_p2 == j:
				print(person[i - 1][j - 1])

	match(p1, p2)
