#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from main import *
from os import _exit

class Gui():
	def __init__(self):
		self.window = Tk()
		self.window.title('Simple Game')

		self.frame_1 = Frame(self.window)
		self.frame_1.grid()

		self.list_1 = ['Name        ', 'Health       ', 'Precision   ','Punch       ', 'Kick          ', 'Endurance']
		self.list_2 = [p1.name, '[  ' + str(p1.health) + ' ]', '[' + str(p1.precision) + '%]', '[   ' + str(p1.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']
		self.list_3 = [p2.name, '[  ' + str(p2.health) + ' ]', '[' + str(p2.precision) + '%]', '[   ' + str(p2.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']

		self.list_label = []

		for i in range(30):
			self.list_label.append(0)

		j = 0

		for i in range(6):
			self.list_label[j] = Label(self.frame_1, text = self.list_1[i], width = 9)
			self.list_label[j].grid(row = i, column = 0)
			j += 1
			self.list_label[j] = Label(self.frame_1, text = self.list_2[i], width = 9)
			self.list_label[j].grid(row = i, column = 1)
			j += 1
			self.list_label[j] = Label(self.frame_1, width = 40)
			self.list_label[j].grid(row = i, column = 2)
			j += 1
			self.list_label[j] = Label(self.frame_1, text = self.list_1[i], width = 9)
			self.list_label[j].grid(row = i, column = 3)
			j += 1
			self.list_label[j] = Label(self.frame_1, text = self.list_3[i], width = 9)
			self.list_label[j].grid(row = i, column = 4)
			j += 1

		self.frame_2 = Frame(self.window)
		self.frame_2.grid()

		self.image = PhotoImage(file = './Image/' + 'person_start.gif')
		self.label = Label(self.frame_2, image = self.image)
		self.label.grid()

		self.frame_3 = Frame(self.window)
		self.frame_3.grid()

		self.list_text = ['Удар рукой','Удар ногой', 'Блок', 'Ждать', 'Выйти']
		self.list_command = [self.p1_punch, self.p1_kick, self.p1_block, self.p1_wait, self.window.quit]

		for i in range(5):
			Button(self.frame_3, text = self.list_text[i], width = 12, command = self.list_command[i]).grid(row = 0, column = i)

	def p1_punch(self):
		life_p2 = p2.health

		p1.punch(p2)

		if p2.endurance >= 4:
			p2.kick(p1)
			self.image = PhotoImage(file = './Image/' + 'person_punch_kick.gif')

		elif p2.endurance >= 3:
			p2.punch(p1)
			self.image = PhotoImage(file = './Image/' + 'person_punch_punch.gif')

		else:
			if p2.block():
				p2.health = life_p2
			self.image = PhotoImage(file = './Image/' + 'person_punch_block.gif')

		self.list_label[6]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
		self.list_label[9]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
		self.list_label[26]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
		self.list_label[29]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'

		self.label['image'] = self.image

		if p1.health == 0 or p2.health == 0:
			if p1.health == 0 and p2.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_death.gif')
			elif p1.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_win.gif')
			else:
				self.image = PhotoImage(file = './Image/' + 'person_win_death.gif')
			self.label['image'] = self.image
			sleep(2)

	def p1_kick(self):
		life_p2 = p2.health

		p1.kick(p2)

		if p2.endurance >= 4:
			p2.kick(p1)
			self.image = PhotoImage(file = './Image/' + 'person_kick_kick.gif')

		elif p2.endurance >= 3:
			p2.punch(p1)
			self.image = PhotoImage(file = './Image/' + 'person_kick_punch.gif')

		else:
			if p2.block():
				p2.health = life_p2
			self.image = PhotoImage(file = './Image/' + 'person_kick_block.gif')

		self.list_label[6]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
		self.list_label[9]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
		self.list_label[26]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
		self.list_label[29]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'

		self.label['image'] = self.image

		if p1.health == 0 or p2.health == 0:
			if p1.health == 0 and p2.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_death.gif')
			elif p1.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_win.gif')
			else:
				self.image = PhotoImage(file = './Image/' + 'person_win_death.gif')
			self.label['image'] = self.image
			sleep(2)		

	def p1_block(self):
		life_p1 = p1.health

		action = p1.block()

		if p2.endurance >= 4:
			p2.kick(p1)
			self.image = PhotoImage(file = './Image/' + 'person_block_kick.gif')
			
		elif p2.endurance >= 3:
			p2.punch(p1)
			self.image = PhotoImage(file = './Image/' + 'person_block_punch.gif')

		else:
			p2.block()
			self.image = PhotoImage(file = './Image/' + 'person_block_block.gif')

		if action == 3:
			p1.health = life_p1

		self.list_label[6]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
		self.list_label[9]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
		self.list_label[26]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
		self.list_label[29]['text'] = '[  ' + str(p2.endurance).rjust(3) + ' ]'

		self.label['image'] = self.image

		if p1.health == 0 or p2.health == 0:
			if p1.health == 0 and p2.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_death.gif')
			elif p1.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_win.gif')
			else:
				self.image = PhotoImage(file = './Image/' + 'person_win_death.gif')
			self.label['image'] = self.image
			sleep(2)

	def p1_wait(self):
		p1.wait()

		if p2.endurance >= 4:
			p2.kick(p1)
			self.image = PhotoImage(file = './Image/' + 'person_wait_kick.gif')

		elif p2.endurance >= 3:
			p2.punch(p1)
			self.image = PhotoImage(file = './Image/' + 'person_wait_punch.gif')

		else:
			p2.block()
			self.image = PhotoImage(file = './Image/' + 'person_wait_block.gif')

		self.list_label[6]['text'] = '[  ' + str(p1.health).rjust(3) + ' ]'
		self.list_label[9]['text'] = '[  ' + str(p2.health).rjust(3) + ' ]'
		self.list_label[26]['text'] = '[  ' + str(p1.endurance).rjust(3) + ' ]'
		self.list_label[29]['text'] = '[  ' + str(p2.endurance).rjust(3)	 + ' ]'

		self.label['image'] = self.image

		if p1.health == 0 or p2.health == 0:
			if p1.health == 0 and p2.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_death.gif')
			elif p1.health == 0:
				self.image = PhotoImage(file = './Image/' + 'person_death_win.gif')
			else:
				self.image = PhotoImage(file = './Image/' + 'person_win_death.gif')
			self.label['image'] = self.image
			sleep(2)

gui = Gui()
gui.window.mainloop()
