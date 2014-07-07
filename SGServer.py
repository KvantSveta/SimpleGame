__author__ = 'j.d.'

from tkinter import *
from classperson import Person
from SGGui import Gui

class Server(Gui):
	"""docstring for Server"""
	def __init__(self, size):
		Gui.__init__(self, size)


p1 = Person('', 15, 0.7, 3, 5, 13)
p2 = Person('', 15, 0.7, 3, 5, 13)

s = Server('460x620')
s.inform(p1, p2)
s.window.mainloop()