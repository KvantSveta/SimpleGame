#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from time import sleep
from sys import argv

p1 = Person('John', 13, 0.7, 3, 5, 0)
p2 = Person('Bot', 13, 0.7, 3, 5, 2)

def update_logic():
	list_function = [
		[action_punch_punch(p1, p2), action_punch_kick(p1, p2), action_punch_block(p1, p2), action_punch_wait(p1, p2)],
		[action_kick_punch(p1, p2), action_kick_kick(p1, p2), action_kick_block(p1, p2), action_kick_wait(p1, p2)],
		[action_block_punch(p1, p2), action_block_kick(p1, p2), action_block_block(p1, p2), action_block_wait(p1, p2)],
		[action_wait_punch(p1, p2), action_wait_kick(p1, p2), action_wait_block(p1, p2), action_wait_wait(p1, p2)],
	]

	for i in range(4):
		for j in range(4):
			label_list[i][j]['text'] = format(list_function[i][j], '.2f')

	min_max = [''] * 4

	for i in range(4):
		min_max[i] = max(list_function[0][i], list_function[1][i], list_function[2][i], list_function[3][i])

	min_index = 0

	for i in range(1, 4):
		if min_max[min_index] > min_max[i]:
			min_index = i

	return(min_index)

def paint_label():
	for i in range(4):
		if i == update_logic():
			logic_label[i]['bg'] = 'red'
		else:
			logic_label[i]['bg'] = '#d9d9d9'

def match():
	paint_label()

	global image_1
	global image_2

	if p1.health == 0 or p2.health == 0:
		button.grab_set()

		if p1.health == 0 and p2.health == 0:
			image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')
		elif p1.health == 0:
			image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_win.gif')
		else:
			image_1 = PhotoImage(file = './Image/' + 'p1_win.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')

		sleep(2)

		label_1['image'] = image_1
		label_2['image'] = image_2

def menu_change():
	list_label[0]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
	list_label[1]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
	list_label[2]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
	list_label[3]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'

def p2_action():
	global image_2

	action = update_logic()

	if action == 0:
		p2.punch(p1)
		image_2 = PhotoImage(file = './Image/' + 'p2_punch.gif')
	elif action == 1:
		p2.kick(p1)
		image_2 = PhotoImage(file = './Image/' + 'p2_kick.gif')
	elif action == 2:
		if p2.block():
			action = 3
		image_2 = PhotoImage(file = './Image/' + 'p2_block.gif')
	else:
		p2.wait()
		image_2 = PhotoImage(file = './Image/' + 'p2_wait.gif')

	label_2['image'] = image_2
	label_2.update()

	return action

def p1_punch():
	global image_1

	life_p2 = p2.health

	action = p2_action()

	p1.punch(p2)

	if action == 3:
		p2.health = life_p2

	menu_change()

	image_1 = PhotoImage(file = './Image/' + 'p1_punch.gif')
	label_1['image'] = image_1
	label_1.update()

	match()

def p1_kick():
	global image_1

	life_p2 = p2.health

	action = p2_action()

	p1.kick(p2)

	if action == 3:
		p2.health = life_p2

	menu_change()

	image_1 = PhotoImage(file = './Image/' + 'p1_kick.gif')
	label_1['image'] = image_1
	label_1.update()

	match()

def p1_block():
	global image_1

	life_p1 = p1.health

	p2_action()

	action = p1.block()

	if action == 3:
		p1.health = life_p1

	menu_change()

	image_1 = PhotoImage(file = './Image/' + 'p1_block.gif')
	label_1['image'] = image_1
	label_1.update()

	match()

def p1_wait():
	global image_1

	p2_action()

	p1.wait()

	menu_change()

	image_1 = PhotoImage(file = './Image/' + 'p1_wait.gif')
	label_1['image'] = image_1
	label_1.update()

	match()

window = Tk()
window.title('Simple Game')

frame_1 = LabelFrame(window)
frame_1.grid()

list_label = [''] * 4

for index, item in enumerate(['Name        ', 'Health       ', 'Endurance']):
	Label(frame_1, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_1, text = item, width = 9).grid(row = index, column = 2)

Label(frame_1, text = p1.name, width = 9).grid(row = 0, column = 1)
Label(frame_1, text = p2.name, width = 9).grid(row = 0, column = 3)

list_label[0] = Label(frame_1, text = '[  ' + str(p1.health) + ' ]', width = 9)
list_label[0].grid(row = 1, column = 1)
list_label[1] = Label(frame_1, text = '[  ' + str(p2.health) + ' ]', width = 9)
list_label[1].grid(row = 1, column = 3)
list_label[2] = Label(frame_1, text = '[  ' + str(p1.endurance) + ' ]', width = 9)
list_label[2].grid(row = 2, column = 1)
list_label[3] = Label(frame_1, text = '[  ' + str(p2.endurance) + ' ]', width = 9)
list_label[3].grid(row = 2, column = 3)

frame_2 = LabelFrame(window)
frame_2.grid()

image_1 = PhotoImage(file = './Image/' + 'p1_start.gif')
image_2 = PhotoImage(file = './Image/' + 'p2_start.gif')
label_1 = Label(frame_2, image = image_1)
label_2 = Label(frame_2, image = image_2)
label_1.grid(row = 0, column = 0)
label_2.grid(row = 0, column = 1)

frame_3 = Frame(window)
frame_3.grid()

list_command = [p1_punch, p1_kick, p1_block, p1_wait]

for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	Button(frame_3, text = action, width = 12, command = list_command[index]).grid(row = 0, column = index)

button = Button(frame_3, text = 'Выйти', width = 12, command = window.quit)
button.grid(row = 0, column = 4)

if len(argv) == 2 and (argv[1] == '-e' or argv[1] == '--extended'):
	from logicbot import *

	super_frame = LabelFrame(window)
	super_frame.grid()

	frame1 = Frame(super_frame, width = 12, height = 12)
	frame1.grid(row = 0, column = 0)

	image_ = PhotoImage(file = './' + 'python.gif')
	Label(frame1, image = image_, width = 66, height = 66).grid()

	frame2 = Frame(super_frame)
	frame2.grid(row = 0, column = 1)

	Label(frame2, text = p2.name).grid(row = 0, columnspan = 4)
	logic_label = [''] * 4
	for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
		logic_label[index] = Label(frame2, text = action, width = 10, height = 3)
		logic_label[index].grid(row = 1, column = index)

	frame3 = Frame(super_frame)
	frame3.grid(row = 1, column = 0)

	Label(frame3, text = p1.name).grid(rowspan = 4, column = 0)
	for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
		Label(frame3, text = action, width = 10, height = 4).grid(row = index, column = 1)

	frame4 = Frame(super_frame)
	frame4.grid(row = 1, column = 1)

	label_list = [[''] * 4] * 4

	list_function = [
		[action_punch_punch(p1, p2), action_punch_kick(p1, p2), action_punch_block(p1, p2), action_punch_wait(p1, p2)],
		[action_kick_punch(p1, p2), action_kick_kick(p1, p2), action_kick_block(p1, p2), action_kick_wait(p1, p2)],
		[action_block_punch(p1, p2), action_block_kick(p1, p2), action_block_block(p1, p2), action_block_wait(p1, p2)],
		[action_wait_punch(p1, p2), action_wait_kick(p1, p2), action_wait_block(p1, p2), action_wait_wait(p1, p2)],
	]

	for i in range(4):
		for j in range(4):
			label_list[i][j] = Label(frame4, width = 8, height = 4, text = format(list_function[i][j], '.2f'))
			label_list[i][j].grid(row = i, column = j)

	min_max = [''] * 4

	for i in range(4):
		min_max[i] = max(list_function[0][i], list_function[1][i], list_function[2][i], list_function[3][i])

	min_index = 0

	for i in range(1, 4):
		if min_max[min_index] > min_max[i]:
			min_index = i

	logic_label[min_index]['bg'] = 'red'

window.mainloop()
