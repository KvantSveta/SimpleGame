__author__ = 'j.d.'

from tkinter import *
from classperson import Person

class Gui():
	"""docstring for Gui"""
	def __init__(self):
		self.window = Tk()
		self.window.geometry('460x620') #window.geometry('336x292+500+100') client
		self.window.title('Simple Game')
		self.window.grid()
		self.frame_info_person = Frame(self.window)
		self.frame_info_person.grid()

		for index, item in enumerate(['Name         ', 'Health        ', 'Endurance ']):
			Label(self.frame_info_person, text = item, width = 9).grid(row = index, column = 0)
			Label(self.frame_info_person, text = item, width = 9).grid(row = index, column = 2)

		self.label_p1_name = Label(self.frame_info_person, text = p1.name, width = 10)
		self.label_p1_name.grid(row = 0, column = 1)
		self.label_p2_name = Label(self.frame_info_person, text = p2.name, width = 10)
		self.label_p2_name.grid(row = 0, column = 3)

		self.list_label = [''] * 4

		self.list_label[0] = Label(self.frame_info_person, text = str(p1.health), width = 10)
		self.list_label[0].grid(row = 1, column = 1)
		self.list_label[1] = Label(self.frame_info_person, text = str(p2.health), width = 10)
		self.list_label[1].grid(row = 1, column = 3)
		self.list_label[2] = Label(self.frame_info_person, text = str(p1.endurance), width = 10)
		self.list_label[2].grid(row = 2, column = 1)
		self.list_label[3] = Label(self.frame_info_person, text = str(p2.endurance), width = 10)
		self.list_label[3].grid(row = 2, column = 3)

		self.frame_image = LabelFrame(self.window)
		self.frame_image.grid(sticky = N)

		self.image_1 = PhotoImage(file = './Image/' + 'p1_start.gif')
		self.image_2 = PhotoImage(file = './Image/' + 'p2_start.gif')
		self.label_1 = Label(self.frame_image, image = self.image_1)
		self.label_2 = Label(self.frame_image, image = self.image_2)
		self.label_1.grid(row = 0, column = 0)
		self.label_2.grid(row = 0, column = 1)


p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

g = Gui()
g.window.mainloop()