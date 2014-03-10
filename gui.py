#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person

p1 = Person('John', 1, 70, 3, 5, 13)
p2 = Person('Bot', 1, 70, 3, 5, 13)

def match():
	global image

	if p1.health == 0 or p2.health == 0:
		if p1.health == 0 and p2.health == 0:
			image = PhotoImage(file = './Image/' + 'person_death_death.gif')
		elif p1.health == 0:
			image = PhotoImage(file = './Image/' + 'person_death_win.gif')
		else:
			image = PhotoImage(file = './Image/' + 'person_win_death.gif')
		label['image'] = image

		button.grab_set()

def menu_change():
	list_label[0]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
	list_label[1]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
	list_label[2]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
	list_label[3]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'

def p1_punch():
	global image

	life_p2 = p2.health

	p1.punch(p2)

	if p2.endurance >= 4:
		p2.kick(p1)
		image = PhotoImage(file = './Image/' + 'person_punch_kick.gif')

	elif p2.endurance >= 3:
		p2.punch(p1)
		image = PhotoImage(file = './Image/' + 'person_punch_punch.gif')

	else:
		if p2.block():
			p2.health = life_p2
		image = PhotoImage(file = './Image/' + 'person_punch_block.gif')

	menu_change()

	label['image'] = image

	match()

def p1_kick():
	global image

	life_p2 = p2.health

	p1.kick(p2)

	if p2.endurance >= 4:
		p2.kick(p1)
		image = PhotoImage(file = './Image/' + 'person_kick_kick.gif')

	elif p2.endurance >= 3:
		p2.punch(p1)
		image = PhotoImage(file = './Image/' + 'person_kick_punch.gif')

	else:
		if p2.block():
			p2.health = life_p2
		image = PhotoImage(file = './Image/' + 'person_kick_block.gif')

	menu_change()

	label['image'] = image

	match()

def p1_block():
	global image

	life_p1 = p1.health

	action = p1.block()

	if p2.endurance >= 4:
		p2.kick(p1)
		image = PhotoImage(file = './Image/' + 'person_block_kick.gif')
		
	elif p2.endurance >= 3:
		p2.punch(p1)
		image = PhotoImage(file = './Image/' + 'person_block_punch.gif')

	else:
		p2.block()
		image = PhotoImage(file = './Image/' + 'person_block_block.gif')

	if action == 3:
		p1.health = life_p1

	menu_change()

	label['image'] = image

	match()

def p1_wait():
	global image

	p1.wait()

	if p2.endurance >= 4:
		p2.kick(p1)
		image = PhotoImage(file = './Image/' + 'person_wait_kick.gif')

	elif p2.endurance >= 3:
		p2.punch(p1)
		image = PhotoImage(file = './Image/' + 'person_wait_punch.gif')

	else:
		p2.block()
		image = PhotoImage(file = './Image/' + 'person_wait_block.gif')

	menu_change()

	label['image'] = image

	match()

window = Tk()
window.title('Simple Game')

frame_1 = Frame(window)
frame_1.grid()

list_1 = ['Name        ', 'Health       ', 'Precision   ','Punch       ', 'Kick          ', 'Endurance']
list_2 = [p1.name, '[  ' + str(p1.health) + ' ]', '[' + str(p1.precision) + '%]', '[   ' + str(p1.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']
list_3 = [p2.name, '[  ' + str(p2.health) + ' ]', '[' + str(p2.precision) + '%]', '[   ' + str(p2.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']

list_label = [''] * 4 

for i in range(6):	
	Label(frame_1, text = list_1[i], width = 9).grid(row = i, column = 0)

	if i in [1, 5]:
		k = 1 % i
		list_label[k] = Label(frame_1, text = list_2[i], width = 9)
		list_label[k].grid(row = i, column = 1)
	else:
		Label(frame_1, text = list_2[i], width = 9).grid(row = i, column = 1)

	Label(frame_1, width = 40).grid(row = i, column = 2)
	Label(frame_1, text = list_1[i], width = 9).grid(row = i, column = 3)
	Label(frame_1, text = list_3[i], width = 9).grid(row = i, column = 4)

frame_2 = Frame(window)
frame_2.grid()

image = PhotoImage(file = './Image/' + 'person_start.gif')
label = Label(frame_2, image = image)
label.grid()

frame_3 = Frame(window)
frame_3.grid()

list_text = ['Удар рукой','Удар ногой', 'Блок', 'Ждать', 'Выйти']
list_command = [p1_punch, p1_kick, p1_block, p1_wait, window.quit]

for i in range(4):
	Button(frame_3, text = list_text[i], width = 12, command = list_command[i]).grid(row = 0, column = i)

button = Button(frame_3, text = list_text[4], width = 12, command = list_command[4])
button.grid(row = 0, column = 4)

window.mainloop()
