__author__ = 'j.d.'

from tkinter import *

window = Tk()
window.title('Logic Bot')

frame_1 = Frame(width = 12, height = 12)
frame_1.grid(row = 0, column = 0)

image = PhotoImage(file = './' + 'python.gif')
Label(frame_1, image = image).grid()

frame_2 = Frame()
frame_2.grid(row = 0, column = 1)

Label(frame_2, text = 'Bot', width = 12, height = 3).grid(row = 0, columnspan = 4)
Label(frame_2, text = 'Удар рукой', width = 12, height = 3).grid(row = 1, column = 0)
Label(frame_2, text = 'Удар ногой', width = 12, height = 3).grid(row = 1, column = 1)
Label(frame_2, text = 'Блок', width = 12, height = 3).grid(row = 1, column = 2)
Label(frame_2, text = 'Ждать', width = 12, height = 3).grid(row = 1, column = 3)

frame_3 = Frame()
frame_3.grid(row = 1, column = 0)

Label(frame_3, text = 'John', width = 10, height = 6).grid(rowspan = 4, column = 0)
Label(frame_3, text = 'Удар рукой', width = 10, height = 6).grid(row = 0, column = 1)
Label(frame_3, text = 'Удар ногой', width = 10, height = 6).grid(row = 1, column = 1)
Label(frame_3, text = 'Блок', width = 10, height = 6).grid(row = 2, column = 1)
Label(frame_3, text = 'Ждать', width = 10, height = 6).grid(row = 3, column = 1)

frame_4 = Frame()
frame_4.grid(row = 1, column = 1)

window.mainloop()