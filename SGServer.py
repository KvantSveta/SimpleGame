#!/usr/bin/env python3

__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from SGGui import Gui

class Server(Gui):
	"""docstring for Server"""
	def __init__(self, size):
		Gui.__init__(self, size)

		self.frame_payoff_matrix = LabelFrame(self.window)
		self.frame_payoff_matrix.grid(sticky = N)

		self.frame1 = Frame(self.frame_payoff_matrix, width = 12, height = 12)
		self.frame1.grid(row = 0, column = 0)

		self.label_price_game = Label(self.frame1, text = 'Цена Игры')
		self.label_price_game.grid()

		self.frame2 = Frame(self.frame_payoff_matrix)
		self.frame2.grid(row = 0, column = 1, sticky = N)

		self.label_p2_name_matrix = Label(self.frame2, text = p2.name, height = 2)
		self.label_p2_name_matrix.grid(row = 0, columnspan = 4)

		self.logic_label_1 = [''] * 4
		for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
			self.logic_label_1[index] = Label(self.frame2, text = action, width = 10, height = 4)
			self.logic_label_1[index].grid(row = 1, column = index)

		self.frame3 = Frame(self.frame_payoff_matrix)
		self.frame3.grid(row = 1, column = 0, sticky = N)

		self.label_p1_name_matrix = Label(self.frame3, text = p1.name, width = 4)
		self.label_p1_name_matrix.grid(rowspan = 4, column = 0)

		self.logic_label_2 = [''] * 4
		for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
			self.logic_label_2[index] = Label(self.frame3, text = action, width = 10, height = 4)
			self.logic_label_2[index].grid(row = index, column = 1)

		self.frame4 = Frame(self.frame_payoff_matrix)
		self.frame4.grid(row = 1, column = 1, sticky = N)

		self.label_list = [[''] * 4, [''] * 4, [''] * 4, [''] * 4]

		for i in range(4):
			for j in range(4):
				self.label_list[i][j] = Label(self.frame4, width = 10, height = 4, text = '')
				self.label_list[i][j].grid(row = i, column = j)


p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

s = Server('460x620')
s.inform(p1, p2)
s.window.mainloop()

