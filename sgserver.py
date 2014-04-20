#!/usr/bin/python3.3

__author__ = 'j.d.'

from os import *
from tkinter import *
from socket import *
from ssl import *
from random import random
from threading import Thread
from time import sleep
from classperson import Person
from logicbot import *

context = SSLContext(PROTOCOL_TLSv1)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')
#context.load_cert_chain(certfile='/etc/ssl/certs/DigiCert_High_Assurance_EV_Root_CA.pem', keyfile='/home/jd/SimpleGame/key')

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind(('', 50007))
sockobj.listen(5)

p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

def mixed_strategy(list_function):
	min_element = min(min(list_function))

	for i in range(4):
		for j in range(4):
			list_function[i][j] -= min_element

	lf = list_function

	simplex_table = [
		['базис', 'B',     'x1',     'x2',     'x3',     'x4', 'x5', 'x6', 'x7', 'x8'],
		['x5'   ,   1, lf[0][0], lf[0][1], lf[0][2], lf[0][3],    1,    0,    0,    0], 
		['x6'   ,   1, lf[1][0], lf[1][1], lf[1][2], lf[1][3],    0,    1,    0,    0], 
		['x7'   ,   1, lf[2][0], lf[2][1], lf[2][2], lf[2][3],    0,    0,    1,    0], 
		['x8'   ,   1, lf[3][0], lf[3][1], lf[3][2], lf[3][3],    0,    0,    0,    1],
		['F(x)' ,   0,       -1,       -1,       -1,       -1,    0,    0,    0,    0]
	]

	while True:
		leading_column = 2

		for i in range(3, 6):
			if simplex_table[5][leading_column] > simplex_table[5][i]:
				leading_column = i

		temp = []

		leading_row = 0

		for i in range(1, 5):
			if simplex_table[i][leading_column] > 0:
				leading_row = i
				break
		else:
			print('Решения нет!!!')
			_exit(1)

		for i in range(leading_row, 5):
			if simplex_table[i][leading_column] > 0:
				if simplex_table[i][1] / simplex_table[i][leading_column] < simplex_table[leading_row][1] / simplex_table[leading_row][leading_column]:
					leading_row = i

		allow_element = simplex_table[leading_row][leading_column]

		simplex_table[leading_row][0] = simplex_table[0][leading_column]

		temp_table = [[''] * 10, [''] * 10, [''] * 10, [''] * 10, [''] * 10, [''] * 10]

		for i in range(6):
			for j in range(10):
				temp_table[i][j] = simplex_table[i][j]

		for i in range(1, 6):
			for j in range(1, 10):
				if i == leading_row:
					simplex_table[i][j] = temp_table[i][j] / allow_element
				else:
					simplex_table[i][j] = temp_table[i][j] - temp_table[leading_row][j] * temp_table[i][leading_column] / allow_element

		if min(simplex_table[5][1:10]) >= 0:
			from pprint import pprint
			X = [0] * 4

			for i, value in enumerate(['x1', 'x2', 'x3', 'x4']):
				for j in range(1, 5):
					if simplex_table[j][0] == value:
						X[i] = simplex_table[j][1]
						break

			Y = simplex_table[5][6:10]
			F = simplex_table[5][1]
			G = 1 / F
			V = G + min_element

			P = [''] * 4
			Q = [''] * 4

			for i in range(4):
				P[i] = G * Y[i]
				Q[i] = G * X[i]

			for i in range(4):
				P[i] = round(P[i], 4)
				Q[i] = round(Q[i], 4)

			for i, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
				logic_label_1[i]['text'] = action + '\n' + str(Q[i])
				logic_label_2[i]['text'] = action + '\n' + str(P[i])
				logic_label_1[i].update()
				logic_label_2[i].update()

			label_price_game['text'] = 'Цена Игры' + '\n' + str(round(V, 4))
			label_price_game.update()

			return [P, Q]

def pure_strategy(list_function):
	for i in range(4):
		for j in range(4):
			label_list[i][j]['text'] = str(round(list_function[i][j], 2))
			label_list[i][j].update()

	min_max = ['', '', '', '']
	max_min = ['', '', '', '']

	for i in range(4):
		min_max[i] = max(list_function[0][i], list_function[1][i], list_function[2][i], list_function[3][i])
		max_min[i] = min(list_function[i][0], list_function[i][1], list_function[i][2], list_function[i][3])

	min_index = max_index = 0

	for i in range(1, 4):
		if min_max[min_index] > min_max[i]:
			min_index = i
		if max_min[max_index] < max_min[i]:
			max_index = i

	if min_max[min_index] == max_min[max_index]:
		for i, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
			logic_label_1[i]['text'] = action
			logic_label_2[i]['text'] = action
			logic_label_1[i].update()
			logic_label_2[i].update()
		label_price_game['text'] = 'Цена Игры' + '\n' + str(min_max[min_index])
		label_price_game.update()
		return [True, min_index, max_index]
	else:
		return [False, 0, 0]

def fighting(sockobj):
	new_socket, address = sockobj.accept()
	connection = context.wrap_socket(new_socket, server_side=True)

	print('Игрок подключился к серверу ', address)

	data = connection.recv(1024)

	p1_name, p1_hash_password = data.decode().split()

	p2_name = 'Bot'

	label_p1_name['text'] = label_p1_name_matrix['text'] = p1_name
	label_p2_name['text'] = label_p2_name_matrix['text'] = p2_name

	data = p1_name + ' ' + p2_name + ' ' + str(p1.health) + ' ' + str(p2.health) + ' ' + str(p1.endurance) + ' ' + str(p2.endurance)

	connection.send(data.encode())

	while p1.health and p2.health:
		p1_life = p1.health
		p2_life = p2.health

		list_function = [
			[action_punch_punch(p1, p2), action_punch_kick(p1, p2), action_punch_block(p1, p2), action_punch_wait(p1, p2)],
			[action_kick_punch(p1, p2), action_kick_kick(p1, p2), action_kick_block(p1, p2), action_kick_wait(p1, p2)],
			[action_block_punch(p1, p2), action_block_kick(p1, p2), action_block_block(p1, p2), action_block_wait(p1, p2)],
			[action_wait_punch(p1, p2), action_wait_kick(p1, p2), action_wait_block(p1, p2), action_wait_wait(p1, p2)],
		]

		saddle_point, min_index, max_index = pure_strategy(list_function)

		if saddle_point:
			for i in range(4):
				if i == min_index:
					logic_label_1[i]['bg'] = '#D51A3F'
				else:
					logic_label_1[i]['bg'] = '#d9d9d9'
				logic_label_1[i].update()

			for i in range(4):
				if i == max_index:
					logic_label_2[i]['bg'] = '#5379C2'
				else:
					logic_label_2[i]['bg'] = '#d9d9d9'
				logic_label_2[i].update()

		else:
			P, Q = mixed_strategy(list_function)

			for i in range(4):
				if Q[i]:
					logic_label_1[i]['bg'] = '#D51A3F'
				else:
					logic_label_1[i]['bg'] = '#d9d9d9'
				logic_label_1[i].update()

			for i in range(4):
				if P[i]:
					logic_label_2[i]['bg'] = '#5379C2'
				else:
					logic_label_2[i]['bg'] = '#d9d9d9'
				logic_label_2[i].update()

		action = connection.recv(1024)

		global image_1
		global image_2

		p1_action = action.decode()

		if p1_action == 'punch':
			p1.punch(p2)
			image_1 = PhotoImage(file = './Image/' + 'p1_punch.gif')
		elif p1_action == 'kick':
			p1.kick(p2)
			image_1 = PhotoImage(file = './Image/' + 'p1_kick.gif')
		elif p1_action == 'block':
			action = p1.block()
			image_1 = PhotoImage(file = './Image/' + 'p1_block.gif')
		else:
			p1.wait()
			image_1 = PhotoImage(file = './Image/' + 'p1_wait.gif')

		if saddle_point:
			p2_action = min_index

			if p2_action == 0:
				p2.punch(p1)
				image_2 = PhotoImage(file = './Image/' + 'p2_punch.gif')
			elif p2_action == 1:
				p2.kick(p1)
				image_2 = PhotoImage(file = './Image/' + 'p2_kick.gif')
			elif p2_action == 2:
				if p2.block():
					p2.health = p2_life
				image_2 = PhotoImage(file = './Image/' + 'p2_block.gif')
			else:
				p2.wait()
				image_2 = PhotoImage(file = './Image/' + 'p2_wait.gif')

			if action == 3:
				p1.health = p1_life

		else:
			random_choice = random()

			if random_choice <= Q[0]:
				p2.punch(p1)
				image_2 = PhotoImage(file = './Image/' + 'p2_punch.gif')
				min_index = 0
			elif random_choice <= Q[0] + Q[1]:
				p2.kick(p1)
				image_2 = PhotoImage(file = './Image/' + 'p2_kick.gif')
				min_index = 1
			elif random_choice <= Q[0] + Q[1] + Q[2]:
				if p2.block():
					p2.health = p2_life
				image_2 = PhotoImage(file = './Image/' + 'p2_block.gif')
				min_index = 2
			else:
				p2.wait()
				image_2 = PhotoImage(file = './Image/' + 'p2_wait.gif')
				min_index = 3

			if action == 3:
				p1.health = p1_life

		label_1['image'] = image_1
		label_2['image'] = image_2

		label_1.update()
		label_2.update()

		list_label[0]['text'] = str(p1.health)
		list_label[1]['text'] = str(p2.health)
		list_label[2]['text'] = str(p1.endurance)
		list_label[3]['text'] = str(p2.endurance)

		for i in range(4):
			list_label[i].update()

		data = str(p1.health) + ' ' + str(p2.health) + ' ' + str(p1.endurance) + ' ' + str(p2.endurance) + ' ' + str(min_index)

		connection.send(data.encode())

		if p1.health == 0 or p2.health == 0:
			sleep(3)

			if p1.health == 0 and p2.health == 0:
				image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
				image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')
			elif p1.health == 0:
				image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
				image_2 = PhotoImage(file = './Image/' + 'p2_win.gif')
			else:
				image_1 = PhotoImage(file = './Image/' + 'p1_win.gif')
				image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')

			label_1['image'] = image_1
			label_2['image'] = image_2

			label_1.update()
			label_2.update()

			for i, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
				logic_label_1[i]['text'] = action
				logic_label_2[i]['text'] = action
				logic_label_1[i].update()
				logic_label_2[i].update()

			label_price_game['text'] = 'Цена Игры'
			label_price_game.update()

			for i in range(4):
				logic_label_1[i]['bg'] = '#d9d9d9'
				logic_label_2[i]['bg'] = '#d9d9d9'
				logic_label_1[i].update()
				logic_label_2[i].update()

			for i in range(4):
				for j in range(4):
					label_list[i][j]['text'] = ''

			connection.shutdown(SHUT_RDWR)
			connection.close()

			return

window = Tk()
window.geometry('460x620')
window.title('Simple Game')
window.grid()

Thread(target = fighting, args = (sockobj,)).start()

frame_info_person = Frame(window)
frame_info_person.grid(sticky = N)

for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 2)

label_p1_name = Label(frame_info_person, text = p1.name, width = 10)
label_p1_name.grid(row = 0, column = 1)
label_p2_name = Label(frame_info_person, text = p2.name, width = 10)
label_p2_name.grid(row = 0, column = 3)

list_label = [''] * 4

list_label[0] = Label(frame_info_person, text = str(p1.health), width = 10)
list_label[0].grid(row = 1, column = 1)
list_label[1] = Label(frame_info_person, text = str(p2.health), width = 10)
list_label[1].grid(row = 1, column = 3)
list_label[2] = Label(frame_info_person, text = str(p1.endurance), width = 10)
list_label[2].grid(row = 2, column = 1)
list_label[3] = Label(frame_info_person, text = str(p2.endurance), width = 10)
list_label[3].grid(row = 2, column = 3)

frame_image = LabelFrame(window)
frame_image.grid(sticky = N)

image_1 = PhotoImage(file = './Image/' + 'p1_start.gif')
image_2 = PhotoImage(file = './Image/' + 'p2_start.gif')
label_1 = Label(frame_image, image = image_1)
label_2 = Label(frame_image, image = image_2)
label_1.grid(row = 0, column = 0)
label_2.grid(row = 0, column = 1)

frame_payoff_matrix = LabelFrame(window)
frame_payoff_matrix.grid(sticky = N)

frame1 = Frame(frame_payoff_matrix, width = 12, height = 12)
frame1.grid(row = 0, column = 0)

label_price_game = Label(frame1, text = 'Цена Игры')
label_price_game.grid()

frame2 = Frame(frame_payoff_matrix)
frame2.grid(row = 0, column = 1, sticky = N)

label_p2_name_matrix = Label(frame2, text = p2.name, height = 2)
label_p2_name_matrix.grid(row = 0, columnspan = 4)

logic_label_1 = [''] * 4
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	logic_label_1[index] = Label(frame2, text = action, width = 10, height = 4)
	logic_label_1[index].grid(row = 1, column = index)

frame3 = Frame(frame_payoff_matrix)
frame3.grid(row = 1, column = 0, sticky = N)

label_p1_name_matrix = Label(frame3, text = p1.name, width = 4)
label_p1_name_matrix.grid(rowspan = 4, column = 0)

logic_label_2 = [''] * 4
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	logic_label_2[index] = Label(frame3, text = action, width = 10, height = 4)
	logic_label_2[index].grid(row = index, column = 1)

frame4 = Frame(frame_payoff_matrix)
frame4.grid(row = 1, column = 1, sticky = N)

label_list = [[''] * 4, [''] * 4, [''] * 4, [''] * 4]

for i in range(4):
	for j in range(4):
		label_list[i][j] = Label(frame4, width = 10, height = 4, text = '')
		label_list[i][j].grid(row = i, column = j)

window.mainloop()
