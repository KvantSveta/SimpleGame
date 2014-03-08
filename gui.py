#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
import sys
from main import *

def quit():
	print('Hello, I must be going...')
	#sys.exit()

window = Tk()
window.title('Simple Game')
'''
win1 = Toplevel()
lab1 = Label(win1, text = 'Здесь будет обображена стратегия бота')
lab1.pack()
'''
frame_1 = Frame()
frame_1.grid()

length = 11
tab = ' ' * 44

Label(frame_1, text = 'Name'.ljust(length) + p1.name.ljust(7)).grid(row = 0, column = 0)
Label(frame_1, text = 'Name'.ljust(length) + p2.name.ljust(7)).grid(row = 0, column = 10)
Label(frame_1, text = 'Health'.ljust(length) + '[ ' + str(p1.health).rjust(2) + ' ]').grid(row = 1, column = 0)
Label(frame_1, text = 'Health'.ljust(length) + '[' + str(p2.health).rjust(2) + ' ]').grid(row = 1, column = 10)
Label(frame_1, text = 'Precision'.ljust(length) + '[' + str(p1.precision) + '%]').grid(row = 2, column = 0)
Label(frame_1, text = 'Precision'.ljust(length) + '[' + str(p2.precision) + '%]').grid(row = 2, column = 8)
Label(frame_1, text = 'Punch'.ljust(length) + '[ ' + str(p1.hand) + ' ]').grid(row = 3, column = 0)
Label(frame_1, text = 'Punch'.ljust(length) + '[ ' + str(p2.hand) + ' ]').grid(row = 3, column = 10)
Label(frame_1, text = 'Kick'.ljust(length) + '[ ' + str(p1.leg) + ' ]').grid(row = 4, column = 0) 
Label(frame_1, text = 'Kick'.ljust(length) + '[ ' + str(p2.leg) + ' ]').grid(row = 4, column = 6)
Label(frame_1, text = 'Endurance'.ljust(length) + '[' + str(p1.endurance).rjust(2) + ' ]').grid(row = 5, column = 0)
Label(frame_1, text = 'Endurance'.ljust(length) + '[' + str(p2.endurance).rjust(2) + ' ]').grid(row = 5, column = 4)

image = PhotoImage(file = './Image/' + 'person_start.gif')
Label(window, image = image).grid()

frame_2 = Frame()
frame_2.grid()

button1 = Button(frame_2, text = 'Удар рукой', command = p1.punch(p2))
button1.grid(row = 0, column = 0)

button2 = Button(frame_2, text = 'Удар ногой', command = p1.kick(p2))
button2.grid(row = 0, column = 1)

button3 = Button(frame_2, text = '   Блок   ', command = p1.block())
button3.grid(row = 0, column = 2)

button4 = Button(frame_2, text = '   Ждать  ', command = p1.wait())
button4.grid(row = 0, column = 3)

button5 = Button(frame_2, text = '   Выйти  ', command = frame_2.quit)
button5.grid(row = 0, column = 4)

window.mainloop()
