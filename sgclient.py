#!/usr/local/bin/python3.4

__author__ = 'j.d.'

from tkinter import *
from tkinter import messagebox
from socket import *
from ssl import *
from time import sleep
from hashlib import sha256
from classperson import Person

host = '127.0.0.1'
port = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
ssl_sockobj = wrap_socket(sockobj, ca_certs='cert.pem', cert_reqs=CERT_REQUIRED)

try:
	ssl_sockobj.connect((host, port))
except ConnectionRefusedError:
	ssl_sockobj.connect(('192.168.1.10', port))


window = Tk()
window.geometry('336x292+500+100')
window.title('Simple Game')
window.grid()

def authorization():
	name = entry_name.get()
	password = entry_password.get()

	if (1 <= len(name) <= 10) and (len(password) >= 6):
		solt = 'python'
		password += solt

		hash_sha256 = sha256(password.encode())
		hash_password = hash_sha256.hexdigest()

		data = name + ' ' + hash_password

		ssl_sockobj.send(data.encode())

		data = ssl_sockobj.recv(1024)

		data = data.decode().split()

		messagebox.showinfo(data[0], data[1:])

		if data[0] == 'Success':	
			window.destroy()

start_frame = Frame()
start_frame.grid(padx = 84, pady = 80, sticky = NSEW)

Label(start_frame, text = 'Введите имя:', width = 20, font = 'Helvetica 10').grid()

entry_name = Entry(start_frame, width = 23, font = 'Helvetica 10')
entry_name.grid()

Label(start_frame, text = 'Введите пароль:', width = 20, font = 'Helvetica 10').grid()

entry_password = Entry(start_frame, width = 23, font = 'Helvetica 10', show="*")
entry_password.grid()

Button(start_frame, text = 'Player vs Computer', width = 20, command = authorization, font = 'Helvetica 10').grid()
Button(start_frame, text = 'Player vs Player', width = 20, command = window.quit, font = 'Helvetica 10').grid()

window.mainloop()


window = Tk()
window.geometry('336x292+500+100')
window.title('Simple Game')
window.grid()

frame_info_person = Frame(window)
frame_info_person.grid(sticky = N)

for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 0)
	Label(frame_info_person, text = item, width = 9).grid(row = index, column = 2)

data = ssl_sockobj.recv(1024)
start_info = data.decode().split()

Label(frame_info_person, text = start_info[0], width = 10).grid(row = 0, column = 1)
Label(frame_info_person, text = start_info[1], width = 10).grid(row = 0, column = 3)

list_label = [''] * 4

list_label[0] = Label(frame_info_person, text = str(start_info[2]), width = 10)
list_label[0].grid(row = 1, column = 1)
list_label[1] = Label(frame_info_person, text = str(start_info[3]), width = 10)
list_label[1].grid(row = 1, column = 3)
list_label[2] = Label(frame_info_person, text = str(start_info[4]), width = 10)
list_label[2].grid(row = 2, column = 1)
list_label[3] = Label(frame_info_person, text = str(start_info[5]), width = 10)
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

def fighting(image):
	global image_1
	global image_2

	image_1 = image

	data = ssl_sockobj.recv(1024)
	new_info = data.decode().split()

	list_label[0]['text'] = new_info[0]
	list_label[1]['text'] = new_info[1]
	list_label[2]['text'] = new_info[2]
	list_label[3]['text'] = new_info[3]

	if new_info[4] == 'punch':
		image_2 = PhotoImage(file = './Image/' + 'p2_punch.gif')
	elif new_info[4] == 'kick':
		image_2 = PhotoImage(file = './Image/' + 'p2_kick.gif')
	elif new_info[4] == 'block':
		image_2 = PhotoImage(file = './Image/' + 'p2_block.gif')
	else:
		image_2 = PhotoImage(file = './Image/' + 'p2_wait.gif')

	label_1['image'] = image_1
	label_2['image'] = image_2

	label_1.update()
	label_2.update()

	if int(new_info[0]) == 0 or int(new_info[1]) == 0:
		sleep(2)

		if int(new_info[0]):
			image_1 = PhotoImage(file = './Image/' + 'p1_win.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')
		elif int(new_info[1]):
			image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_win.gif')
		else:
			image_1 = PhotoImage(file = './Image/' + 'p1_death.gif')
			image_2 = PhotoImage(file = './Image/' + 'p2_death.gif')

		label_1['image'] = image_1
		label_2['image'] = image_2

		label_1.update()
		label_2.update()

		ssl_sockobj.close()

def punch():
	if int(list_label[2]['text']) >= 3 and int(list_label[0]['text']) and int(list_label[1]['text']):
		ssl_sockobj.send('punch'.encode())

		image = PhotoImage(file = './Image/' + 'p1_punch.gif')

		fighting(image)

def kick():
	if int(list_label[2]['text']) >= 4 and int(list_label[0]['text']) and int(list_label[1]['text']):
		ssl_sockobj.send('kick'.encode())

		image = PhotoImage(file = './Image/' + 'p1_kick.gif')

		fighting(image)

def block():
	if 	int(list_label[0]['text']) and int(list_label[1]['text']):
		ssl_sockobj.send('block'.encode())

		image = PhotoImage(file = './Image/' + 'p1_block.gif')

		fighting(image)

def wait():
	if 	int(list_label[0]['text']) and int(list_label[1]['text']):
		ssl_sockobj.send('wait'.encode())

		image = PhotoImage(file = './Image/' + 'p1_wait.gif')

		fighting(image)

Button(frame_action, text = 'Удар рукой', width = 7, command = punch).grid(row = 0, column = 0)
Button(frame_action, text = 'Удар ногой', width = 7, command = kick).grid(row = 0, column = 1)
Button(frame_action, text = 'Блок', width = 7, command = block).grid(row = 0, column = 2)
Button(frame_action, text = 'Ждать', width = 7, command = wait).grid(row = 0, column = 3)

window.mainloop()
