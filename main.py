#!/usr/bin/python3.3

from classperson import Person
from display import *
from time import sleep
from event import *
from os import system

system('clear')

p1 = Person('John', 15, 0.7, 3, 5, 13)
p2 = Person('Bot', 15, 0.7, 3, 5, 13)

display(p1, p2)

print(person_start)

while True:
	print('Выберите действие: 1 - удар рукой, 2 - удар ногой, 3 - блок, 4 - ожидать')
	
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
