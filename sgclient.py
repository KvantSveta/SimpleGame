#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from socket import *
from time import sleep

serverHost = '127.0.0.1'
serverPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
try:
	sockobj.connect((serverHost, serverPort))
except ConnectionRefusedError:
	sockobj.connect(('192.168.1.10', serverPort))


window = Tk()
window.geometry('460x292')
window.title('Simple Game')
window.grid()

def get_name():
	name = entry.get()

	sockobj.send(name.encode())

	window.destroy()

start_frame = Frame()
start_frame.grid(padx = 144, pady = 100, sticky = NSEW)

Label(start_frame, text = 'Введите имя:', width = 20, font = 'Helvetica 10').grid()

entry = Entry(start_frame, width = 23, font = 'Helvetica 10')
entry.grid()
entry.insert(0, 'John')

Button(start_frame, text = 'Player vs Computer', width = 20, command = get_name, font = 'Helvetica 10').grid()
Button(start_frame, text = 'Player vs Player', width = 20, command = window.quit, font = 'Helvetica 10').grid()

window.mainloop()


window = Tk()
window.geometry('460x292')
window.title('Simple Game')
window.grid()

frame_info_person = Frame(window)
frame_info_person.grid(sticky = N)

for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 2)

data = sockobj.recv(1024)
start_info = data.decode().split()

Label(frame_info_person, text = start_info[0], width = 10).grid(row = 0, column = 1)
Label(frame_info_person, text = start_info[1], width = 10).grid(row = 0, column = 3)

list_label = ['', '', '', '']

list_label[0] = Label(frame_info_person, text = '[  ' + str(start_info[2]) + '  ]', width = 10)
list_label[0].grid(row = 1, column = 1)
list_label[1] = Label(frame_info_person, text = '[  ' + str(start_info[3]) + '  ]', width = 10)
list_label[1].grid(row = 1, column = 3)
list_label[2] = Label(frame_info_person, text = '[  ' + str(start_info[4]) + '  ]', width = 10)
list_label[2].grid(row = 2, column = 1)
list_label[3] = Label(frame_info_person, text = '[  ' + str(start_info[5]) + '  ]', width = 10)
list_label[3].grid(row = 2, column = 3)

frame_image = LabelFrame(window)
frame_image.grid(sticky = N)

image_1 = PhotoImage(file = './Image/' + 'p1_start.gif')
image_2 = PhotoImage(file = './Image/' + 'p2_start.gif')
label_1 = Label(frame_image, image = image_1)
label_2 = Label(frame_image, image = image_2)
label_1.grid(row = 0, column = 0)
label_2.grid(row = 0, column = 1)

frame_action = Frame(window)
frame_action.grid(sticky = N)

def punch():
	global image_1
	global image_2

	sockobj.send('punch'.encode())

	data = sockobj.recv(1024)
	new_info = data.decode().split()

	list_label[0]['text'] = new_info[0]
	list_label[1]['text'] = new_info[1]
	list_label[2]['text'] = new_info[2]
	list_label[3]['text'] = new_info[3]

	image_1 = PhotoImage(file = './Image/' + 'p1_punch.gif')
	label_1['image'] = image_1
	label_1.update()

	if new_info[4] == 0:
		image_2 = PhotoImage(file = './Image/' + 'p2_punch.gif')
	elif new_info[4] == 1:
		image_2 = PhotoImage(file = './Image/' + 'p2_kick.gif')
	elif new_info[4] == 2:
		image_2 = PhotoImage(file = './Image/' + 'p2_block.gif')
	else:
		image_2 = PhotoImage(file = './Image/' + 'p2_wait.gif')

	label_2['image'] = image_2
	label_2.update()


def kick():
	sockobj.send('kick'.encode())

def block():
	sockobj.send('block'.encode())

def wait():
	sockobj.send('wait'.encode())

Button(frame_action, text = 'Удар рукой', width = 8, command = punch).grid(row = 0, column = 0)
Button(frame_action, text = 'Удар ногой', width = 8, command = kick).grid(row = 0, column = 1)
Button(frame_action, text = 'Блок', width = 8, command = block).grid(row = 0, column = 2)
Button(frame_action, text = 'Ждать', width = 8, command = wait).grid(row = 0, column = 3)
button = Button(frame_action, text = 'Выйти', width = 8, command = window.quit)
button.grid(row = 0, column = 4)

window.mainloop()

sockobj.close()
