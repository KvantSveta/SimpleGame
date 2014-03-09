#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from main import *

class Gui():
	def __init__(self):
		self.window = Tk()
		self.window.title('Simple Game')

		self.frame_1 = Frame(self.window)
		self.frame_1.grid()

		self.list_1 = ['Name        ', 'Health       ', 'Precision   ','Punch       ', 'Kick          ', 'Endurance']
		self.list_2 = [p1.name, '[  ' + str(p1.health) + ' ]', '[' + str(p1.precision) + '%]', '[   ' + str(p1.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']
		self.list_3 = [p2.name, '[  ' + str(p2.health) + ' ]', '[' + str(p2.precision) + '%]', '[   ' + str(p2.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']

		for i in range(6):
			Label(self.frame_1, text = self.list_1[i], width = 9).grid(row = i, column = 0)
			Label(self.frame_1, text = self.list_2[i], width = 9).grid(row = i, column = 1)
			Label(self.frame_1, width = 40).grid(row = i, column = 2)
			Label(self.frame_1, text = self.list_1[i], width = 9).grid(row = i, column = 3)
			Label(self.frame_1, text = self.list_3[i], width = 9).grid(row = i, column = 4)

		self.image = PhotoImage(file = './Image/' + 'person_start.gif')
		Label(self.window, image = self.image, width = self.image.width(), height = self.image.height()).grid()

		self.frame_2 = Frame(self.window)
		self.frame_2.grid()

		def p1_punch():
			p1.punch(p2)

		def p1_kick():
			p1.kick(p2)

		self.list_text = ['Удар рукой','Удар ногой', 'Блок', 'Ждать', 'Выйти']
		self.list_command = [p1_punch, p1_kick, p1.block, p1.wait, self.window.quit]

		for i in range(5):
			Button(self.frame_2, text = self.list_text[i], width = 12, command = self.list_command[i]).grid(row = 0, column = i)

gui = Gui()
gui.window.mainloop()
