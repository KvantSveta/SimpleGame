#!/usr/bin/python3.3

__author__ = 'j.d.'

from tkinter import *
import sys

root = Tk()

label = Label(root)
label.config(text = 'Hello GUI world!')
label.pack(side = TOP, expand = YES, fill = BOTH)

button = Button(root, text = 'Hello widget world', command = sys.exit)
# command = root.quit
button.pack(side = LEFT, expand = YES)

root.title('Simple Game')
root.mainloop()