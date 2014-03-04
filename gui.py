#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
import sys
from main import *
#from display import display

def quit():
	print('Hello, I must be going...')
	#sys.exit()

'''
root = Tk()
root.title('Simple Game')
'''
win = Frame()
win.pack()

length = 11
tab = ' ' * 44

label1 = Label(win, text = 'Name'.ljust(length) + p1.name.ljust(7) + tab + 'Name'.ljust(length) + p2.name.ljust(7))
label1.pack(anchor = W)

label2 = Label(win, text = 'Health'.ljust(length) + '[ ' + str(p1.health).rjust(2) + ' ]' + tab + 'Health'.ljust(length) + '[' + str(p2.health).rjust(2) + ' ]')
label2.pack(anchor = W)

label3 = Label(win, text = 'Punch'.ljust(length) + '[ ' + str(p1.hand) + ' ]' + tab + 'Punch'.ljust(length) + '[ ' + str(p2.hand) + ' ]')
label3.pack(anchor = W)

label4 = Label(win, text = 'Kick'.ljust(length) + '[ ' + str(p1.leg) + ' ]' + tab + 'Kick'.ljust(length) + '[ ' + str(p2.leg) + ' ]')
label4.pack(anchor = W)

label5 = Label(win, text = 'Endurance'.ljust(length) + '[' + str(p1.endurance).rjust(2) + ' ]' + tab + 'Endurance'.ljust(length) + '[' + str(p2.endurance).rjust(2) + ' ]')
label5.pack(anchor = W)

button1 = Button(win, text = 'Удар рукой', command = quit)
button1.pack(side = LEFT, expand = YES, fill = X)

button2 = Button(win, text = 'Удар ногой', command = quit)
button2.pack(side = LEFT, expand = YES, fill = X)

button3 = Button(win, text = '   Блок   ', command = quit)
button3.pack(side = LEFT, expand = YES, fill = X)

button4 = Button(win, text = '   Ждать  ', command = win.quit)
button4.pack(side = LEFT, expand = YES, fill = X)

win.mainloop()
