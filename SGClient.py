#!/usr/bin/env python3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from SGGui import Gui

class Server(Gui):
	"""docstring for Server"""
	def __init__(self, size):
		Gui.__init__(self, size)

	def authorization(self):
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
				self.window.destroy()




		self.start_frame = Frame()
		self.start_frame.grid(padx = 84, pady = 80, sticky = NSEW)

		Label(self.start_frame, text = 'Введите имя:', width = 20, font = 'Helvetica 10').grid()

		self.entry_name = Entry(self.start_frame, width = 23, font = 'Helvetica 10')
		self.entry_name.grid()

		Label(self.start_frame, text = 'Введите пароль:', width = 20, font = 'Helvetica 10').grid()

		self.entry_password = Entry(self.start_frame, width = 23, font = 'Helvetica 10', show="*")
		entry_password.grid()

		Button(self.start_frame, text = 'Player vs Computer', width = 20, command = authorization, font = 'Helvetica 10').grid()
		Button(self.start_frame, text = 'Player vs Player', width = 20, command = self.window.quit, font = 'Helvetica 10').grid()




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


		Button(frame_action, text = 'Удар рукой', width = 7, command = punch).grid(row = 0, column = 0)
		Button(frame_action, text = 'Удар ногой', width = 7, command = kick).grid(row = 0, column = 1)
		Button(frame_action, text = 'Блок', width = 7, command = block).grid(row = 0, column = 2)
		Button(frame_action, text = 'Ждать', width = 7, command = wait).grid(row = 0, column = 3)



p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

s = Server('336x292+500+100')
s.inform(p1, p2)
s.window.mainloop()