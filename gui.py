#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
import sys
from main import *
#from display import display

def quit():
	print('Hello, I must be going...')
	#sys.exit()

window = Tk()
window.title('Simple Game')

win1 = Toplevel()
lab1 = Label(win1, text = 'Здесь будет обображена стратегия бота')
lab1.pack()

frame = Frame()
frame.pack()

length = 11
tab = ' ' * 44

label1 = Label(frame, text = 'Name'.ljust(length) + p1.name.ljust(7) + tab + 'Name'.ljust(length) + p2.name.ljust(7))
label1.pack(anchor = W)

label2 = Label(frame, text = 'Health'.ljust(length) + '[ ' + str(p1.health).rjust(2) + ' ]' + tab + 'Health'.ljust(length) + '[' + str(p2.health).rjust(2) + ' ]')
label2.pack(anchor = W)

label3 = Label(frame, text = 'Precision'.ljust(length) + '[' + str(p1.precision) + '%]' + tab +  'Precision'.ljust(length) + '[' + str(p2.precision) + '%]')
label3.pack(anchor = W)

label4 = Label(frame, text = 'Punch'.ljust(length) + '[ ' + str(p1.hand) + ' ]' + tab + 'Punch'.ljust(length) + '[ ' + str(p2.hand) + ' ]')
label4.pack(anchor = W)

label5 = Label(frame, text = 'Kick'.ljust(length) + '[ ' + str(p1.leg) + ' ]' + tab + 'Kick'.ljust(length) + '[ ' + str(p2.leg) + ' ]')
label5.pack(anchor = W)

label6 = Label(frame, text = 'Endurance'.ljust(length) + '[' + str(p1.endurance).rjust(2) + ' ]' + tab + 'Endurance'.ljust(length) + '[' + str(p2.endurance).rjust(2) + ' ]')
label6.pack(anchor = W)

image = PhotoImage(file = './Image/' + 'person_start.gif')
Label(frame, image = image).pack()

button1 = Button(frame, text = 'Удар рукой', command = p1.punch(p2))
button1.pack(side = LEFT, expand = YES, fill = X)

button2 = Button(frame, text = 'Удар ногой', command = p1.kick(p2))
button2.pack(side = LEFT, expand = YES, fill = X)

button3 = Button(frame, text = '   Блок   ', command = p1.block())
button3.pack(side = LEFT, expand = YES, fill = X)

button4 = Button(frame, text = '   Ждать  ', command = p1.wait())
button4.pack(side = LEFT, expand = YES, fill = X)

button5 = Button(frame, text = '   Выйти  ', command = frame.quit)
button5.pack(side = LEFT, expand = YES, fill = X)

frame.mainloop()
