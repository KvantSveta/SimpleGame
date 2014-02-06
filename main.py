#!/usr/bin/python3.3

from classperson import Person, randint
from display import display

def	display(p1, p2):
	length = 9
	tab = '                                       '
	print('Name'.ljust(length), p1.name, end = '')
	#print(tab, end = '')
	print('Name'.rjust(length), p2.name)
	print('Health'.ljust(length), '[', p1.health, ' ]', '    ', tab ,'Health'.ljust(length), '[', p2.health   , ' ]')
	print('Precision'.ljust(length), '[', p1.precision, '%]', '    ', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
	print('Punch'.ljust(length), '[ ', p1.hand, ' ]', '    ', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
	print('Kick'.ljust(length), '[ ', p1.leg, ' ]', '    ', tab, 'Kick'.ljust(length), '[ ', p1.leg, ' ]')
	p1.is_dead()
	print(tab, end = '')
	p2.is_dead()
	print(person_big)
 
def event(p1, p2):
	action = int(input('Действие: '))

	if action == 1:
		p1.punch(p2)
	elif action == 2:
		p1.kick(p2)
	elif action == 3:
		p1.block(p2)
	
def event_2(p1, p2):
	action = randint(1, 3)

	if action == 1:
		p1.punch(p2)
	elif action == 2:
		p1.kick(p2)
	elif action == 3:
		p1.block(p2)

p1 = Person('John', 10, 70, 2, 3)
p2 = Person('Bot', 10, 70, 2, 3)

while True:
	display(p1, p2)
	
	print('Выберите действие: 1 - удар рукой, 2 - удар ногой, 3 - блок')
		
	event(p1, p2)
	event_2(p2, p1)