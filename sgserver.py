#!/usr/bin/python3.3

__author__ = 'j.d.'

from socket import *
from tkinter import *
from classperson import Person
from time import sleep
from logicbot import *
from numpy.linalg import det
from threading import Thread
from os import system

myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(1)

p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

def mixed_strategy(list_function):
	a = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
	b = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
	c = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
	d = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

	for i in range(4):
		for j in range(4):
			if j == 0:
				a[i][j] = 1
			else:
				a[i][j] = float(format(list_function[i][j], '.2f'))
			if j == 1:
				b[i][j] = 1
			else:
				b[i][j] = float(format(list_function[i][j], '.2f'))
			if j == 2:
				c[i][j] = 1
			else:
				c[i][j] = float(format(list_function[i][j], '.2f'))
			if j == 3:
				d[i][j] = 1
			else:
				d[i][j] = float(format(list_function[i][j], '.2f'))

	print(det(a))
	print(det(b))
	print(det(c))
	print(det(d))
	#'''

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
			label_list[i][j].update()

	min_max = ['', '', '', '']

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
			logic_label_1[i]['bg'] = 'red'
		else:
			logic_label_1[i]['bg'] = '#d9d9d9'
		logic_label_1[i].update()

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
		label_1.update()
		label_2.update()

def menu_change():
	list_label[0]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
	list_label[1]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
	list_label[2]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
	list_label[3]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'
	for i in range(4):
		list_label[i].update()

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
window.geometry('460x620')
window.title('Simple Game')
window.grid()

def sock_connect(sockobj):
	#system('./sgclient.py')
	connection, address = sockobj.accept()

	print('Server connected by', address)

	data = connection.recv(1024)

	p1_name = data.decode()

	p2_name = 'Bot'

	label_p1_name['text'] = p1_name
	label_p2_name['text'] = p2_name

	data = p1_name + ' '  + p2_name + ' ' + str(p1.health) + ' ' + str(p2.health) + ' ' + str(p1.endurance) + ' '+ str(p2.endurance)

	connection.send(data.encode())

	connection.close()

Thread(target = sock_connect, args = (sockobj,)).start()
#Thread(target = sock_connect, args = (sockobj,)).start()

frame_info_person = Frame(window)
frame_info_person.grid(sticky = N)

for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 2)

label_p1_name = Label(frame_info_person, text = p1.name, width = 10)
label_p1_name.grid(row = 0, column = 1)
label_p2_name = Label(frame_info_person, text = p2.name, width = 10)
label_p2_name.grid(row = 0, column = 3)

list_label = ['', '', '', '']

list_label[0] = Label(frame_info_person, text = '[  ' + str(p1.health) + '  ]', width = 10)
list_label[0].grid(row = 1, column = 1)
list_label[1] = Label(frame_info_person, text = '[  ' + str(p2.health) + '  ]', width = 10)
list_label[1].grid(row = 1, column = 3)
list_label[2] = Label(frame_info_person, text = '[  ' + str(p1.endurance) + '  ]', width = 10)
list_label[2].grid(row = 2, column = 1)
list_label[3] = Label(frame_info_person, text = '[  ' + str(p2.endurance) + '  ]', width = 10)
list_label[3].grid(row = 2, column = 3)

frame_image = LabelFrame(window)
frame_image.grid(sticky = N)

image_1 = PhotoImage(file = './Image/' + 'p1_start.gif')
image_2 = PhotoImage(file = './Image/' + 'p2_start.gif')
label_1 = Label(frame_image, image = image_1)
label_2 = Label(frame_image, image = image_2)
label_1.grid(row = 0, column = 0)
label_2.grid(row = 0, column = 1)
'''
frame_action = Frame(window)
frame_action.grid(sticky = N)

list_command = [p1_punch, p1_kick, p1_block, p1_wait]

for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	Button(frame_action, text = action, width = 8, command = list_command[index]).grid(row = 0, column = index)

button = Button(frame_action, text = 'Выйти', width = 8, command = window.quit)
button.grid(row = 0, column = 4)
'''
frame_payoff_matrix = LabelFrame(window)
frame_payoff_matrix.grid(sticky = N)

frame1 = Frame(frame_payoff_matrix, width = 12, height = 12)
frame1.grid(row = 0, column = 0)

image_ = PhotoImage(file = './' + 'python.gif')
Label(frame1, image = image_, width = 66, height = 66).grid()

frame2 = Frame(frame_payoff_matrix)
frame2.grid(row = 0, column = 1, sticky = N)

Label(frame2, text = p2.name, height = 2).grid(row = 0, columnspan = 4)
logic_label_1 = ['', '', '', '']
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	logic_label_1[index] = Label(frame2, text = action, width = 10, height = 4)
	logic_label_1[index].grid(row = 1, column = index)

frame3 = Frame(frame_payoff_matrix)
frame3.grid(row = 1, column = 0, sticky = N)

Label(frame3, text = p1.name, width = 4).grid(rowspan = 4, column = 0)
logic_label_2 = ['', '', '', '']
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	logic_label_2[index] = Label(frame3, text = action, width = 10, height = 4)
	logic_label_2[index].grid(row = index, column = 1)

frame4 = Frame(frame_payoff_matrix)
frame4.grid(row = 1, column = 1, sticky = N)

label_list = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

list_function = [
	[action_punch_punch(p1, p2), action_punch_kick(p1, p2), action_punch_block(p1, p2), action_punch_wait(p1, p2)],
	[action_kick_punch(p1, p2), action_kick_kick(p1, p2), action_kick_block(p1, p2), action_kick_wait(p1, p2)],
	[action_block_punch(p1, p2), action_block_kick(p1, p2), action_block_block(p1, p2), action_block_wait(p1, p2)],
	[action_wait_punch(p1, p2), action_wait_kick(p1, p2), action_wait_block(p1, p2), action_wait_wait(p1, p2)],
]

for i in range(4):
	for j in range(4):
		label_list[i][j] = Label(frame4, width = 10, height = 4, text = format(list_function[i][j], '.2f'))
		label_list[i][j].grid(row = i, column = j)

min_max = ['', '', '', '']
max_min = ['', '', '', '']

for i in range(4):
	min_max[i] = max(list_function[0][i], list_function[1][i], list_function[2][i], list_function[3][i])
	max_min[i] = min(list_function[i][0], list_function[i][1], list_function[i][2], list_function[i][3])

min_index = 0
max_index = 0

for i in range(1, 4):
	if min_max[min_index] > min_max[i]:
		min_index = i
	if max_min[max_index] < max_min[i]:
		max_index = i

if -min_max[min_index] == max_min[max_index]:
	pass
else:
	mixed_strategy(list_function)

logic_label_1[min_index]['bg'] = '#D51A3F'
logic_label_2[max_index]['bg'] = '#5379C2'

window.mainloop()

sockobj.close()
