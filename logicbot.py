__author__ = 'j.d.'

from tkinter import *
from classperson import Person

p1 = Person('John', 15, 0.7, 3, 5, 13)
p2 = Person('Bot', 1, 0.7, 3, 5, 13)

def action_punch_punch(p1, p2):
	if p1.endurance >= 3 and p2.endurance >= 3:
		return 0.0
	elif p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	elif p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_punch_kick(p1, p2):
	if p1.endurance >= 3 and p2.endurance >= 5:
		return p1.hand * p1.precision_punch  + (-p2.leg) * p2.precision_kick
	elif p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	elif p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_punch_block(p1, p2):
	if p1.endurance >= 3:
		return p1.hand * p1.precision_punch * (1 - p2.precision_block)
	else:
		return 0.0

def action_punch_wait(p1, p2):
	if p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	else:
		return 0.0

def action_kick_punch(p1, p2):
	if p1.endurance >= 5 and p2.endurance >= 3:
		return p1.leg * p1.precision_kick + (-p2.hand) * p2.precision_punch
	elif p1.endurance >= 5:
		return p1.leg * p1.precision_kick
	elif p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_kick_kick(p1, p2):
	if p1.endurance >= 5 and p2.endurance >= 5:
		return 0.0
	elif p1.endurance >= 5:
		return p1.leg * p1.precision_kick
	elif p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_kick_block(p1, p2):
	if p1.endurance >= 5:
		return p2.leg * p2.precision_kick * (1 - p1.precision_block)
	else:
		return 0.0

def action_kick_wait(p1, p2):
	if p1.endurance >= 5:
		return p2.leg * p2.precision_kick
	else:
		return 0.0

def action_block_punch(p1, p2):
	if p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch * (1 - p1.precision_block)
	else:
		return 0.0

def action_block_kick(p1, p2):
	if p1.endurance >= 5:
		return (-p1.leg) * p1.precision_kick * (1 - p2.precision_block)
	else:
		return 0.0

def action_block_block(p1, p2):
	return 0.0

def action_block_wait(p1, p2):
	return -1.0

def action_wait_punch(p1, p2):
	if p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_wait_kick(p1, p2):
	if p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_wait_block(p1, p2):
	return 1.0

def action_wait_wait(p1, p2):
	return 0.0


window = Tk()
window.title('Logic Bot')

frame_1 = Frame(width = 12, height = 12)
frame_1.grid(row = 0, column = 0)

image = PhotoImage(file = './' + 'python.gif')
Label(frame_1, image = image, width = 66, height = 66).grid()

frame_2 = Frame()
frame_2.grid(row = 0, column = 1)

Label(frame_2, text = 'Bot').grid(row = 0, columnspan = 4)
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	Label(frame_2, text = action, width = 10, height = 3).grid(row = 1, column = index)

frame_3 = Frame()
frame_3.grid(row = 1, column = 0)

Label(frame_3, text = 'John').grid(rowspan = 4, column = 0)
for index, action in enumerate(['Удар рукой', 'Удар ногой', 'Блок', 'Ждать']):
	Label(frame_3, text = action, width = 10, height = 4).grid(row = index, column = 1)

frame_4 = Frame()
frame_4.grid(row = 1, column = 1)

label_list = [''] * 16

for i in range(4):
	for j in range(4):
		k = i * 4 + j
		label_list[k] = Label(frame_4, text = '0', width = 8, height = 4)
		label_list[k].grid(row = i, column = j)

list_function = [
	action_punch_punch(p1, p2), action_punch_kick(p1, p2), action_punch_block(p1, p2), action_punch_wait(p1, p2),
	action_kick_punch(p1, p2), action_kick_kick(p1, p2), action_kick_block(p1, p2), action_kick_wait(p1, p2),
	action_block_punch(p1, p2), action_block_kick(p1, p2), action_block_block(p1, p2), action_block_wait(p1, p2),
	action_wait_punch(p1, p2), action_wait_kick(p1, p2), action_wait_block(p1, p2), action_wait_wait(p1, p2),
	]

for index, function in enumerate(list_function):
	label_list[index]['text'] = format(function, '.2f')

window.mainloop()