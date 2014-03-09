#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
from main import *

window = Tk()
window.title('Simple Game')

frame_1 = Frame(window)
frame_1.grid()

list_1 = ['Name        ', 'Health       ', 'Precision   ','Punch       ', 'Kick          ', 'Endurance']
list_2 = [p1.name, '[  ' + str(p1.health) + ' ]', '[' + str(p1.precision) + '%]', '[   ' + str(p1.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']
list_3 = [p2.name, '[  ' + str(p2.health) + ' ]', '[' + str(p2.precision) + '%]', '[   ' + str(p2.hand) + '  ]', '[   ' + str(p1.leg) + '  ]', '[  ' + str(p1.endurance) + ' ]']

for i in range(6):
	Label(frame_1, text = list_1[i], width = 9).grid(row = i, column = 0)
	Label(frame_1, text = list_2[i], width = 9).grid(row = i, column = 1)
	Label(frame_1, width = 40).grid(row = i, column = 2)
	Label(frame_1, text = list_1[i], width = 9).grid(row = i, column = 3)
	Label(frame_1, text = list_3[i], width = 9).grid(row = i, column = 4)

image = PhotoImage(file = './Image/' + 'person_start.gif')
Label(window, image = image, width = image.width(), height = image.height()).grid()

frame_2 = Frame(window)
frame_2.grid()

list_text = ['Удар рукой','Удар ногой', 'Блок', 'Ждать', 'Выйти']
list_command = [p1.punch(p2), p1.kick(p2), p1.block(), p1.wait(), window.quit]

for i in range(5):
	Button(frame_2, text = list_text[i], width = 12, command = list_command[i]).grid(row = 0, column = i)

window.mainloop()
