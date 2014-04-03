#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from socket import *

serverHost = '127.0.0.1'
serverPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
try:
	sockobj.connect((serverHost, serverPort))
except ConnectionRefusedError:
	sockobj.connect(('192.168.1.10', serverPort))


p1 = Person('John', 15, 0.7, 3, 5, 13)
p2 = Person('Bot', 15, 0.7, 3, 5, 13)

window = Tk()
window.geometry('460x292')
window.title('Simple Game')
window.grid()

frame_info_person = Frame(window)
frame_info_person.grid(sticky = N)

for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 2)

Label(frame_info_person, text = p1.name, width = 10).grid(row = 0, column = 1)
Label(frame_info_person, text = p2.name, width = 10).grid(row = 0, column = 3)

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

frame_action = Frame(window)
frame_action.grid(sticky = N)

def punch():
	sockobj.send('punch'.encode())

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
