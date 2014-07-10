__author__ = 'j.d.'

from tkinter import *

class Gui():
	"""docstring for Gui"""
	def __init__(self, size):
		self.window = Tk()
		self.window.geometry(size)
		self.window.title('Simple Game')
		self.window.grid()
		self.frame_info_person = Frame(self.window)
		self.frame_info_person.grid()

		for index, item in enumerate(['Name\t\t', 'Health\t\t', 'Endurance\t']):
			Label(self.frame_info_person, text = item, width = 9).grid(row = index, column = 0)
			Label(self.frame_info_person, text = item, width = 9).grid(row = index, column = 2)

		self.label_p1_name = Label(self.frame_info_person, text = '', width = 10)
		self.label_p1_name.grid(row = 0, column = 1)
		self.label_p2_name = Label(self.frame_info_person, text = '', width = 10)
		self.label_p2_name.grid(row = 0, column = 3)

		self.list_label = [''] * 4

		self.list_label[0] = Label(self.frame_info_person, text = '', width = 10)
		self.list_label[0].grid(row = 1, column = 1)
		self.list_label[1] = Label(self.frame_info_person, text = '', width = 10)
		self.list_label[1].grid(row = 1, column = 3)
		self.list_label[2] = Label(self.frame_info_person, text = '', width = 10)
		self.list_label[2].grid(row = 2, column = 1)
		self.list_label[3] = Label(self.frame_info_person, text = '', width = 10)
		self.list_label[3].grid(row = 2, column = 3)

		self.frame_image = LabelFrame(self.window)
		self.frame_image.grid(sticky = N)

		self.image_p1 = PhotoImage(file = './Image/' + 'p1_start.gif')
		self.image_p2 = PhotoImage(file = './Image/' + 'p2_start.gif')
		self.label_p1 = Label(self.frame_image, image = self.image_p1)
		self.label_p2 = Label(self.frame_image, image = self.image_p2)
		self.label_p1.grid(row = 0, column = 0)
		self.label_p2.grid(row = 0, column = 1)

	def inform(self, p1, p2):
		self.label_p1_name.text = 'hi'#p1.name
		self.label_p1_name.text = p2.name

		self.list_label[0].text = str(p1.health)
		self.list_label[1].text = str(p2.health)
		self.list_label[2].text = str(p1.endurance)
		self.list_label[3].text = str(p2.endurance)
