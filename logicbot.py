__author__ = 'j.d.'

from tkinter import *

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

label_list = [[''] * 4] * 4

for i in range(4):
	for j in range(4):
		label_list[i][j] = Label(frame_4, text = '0', width = 4, height = 4)
		label_list[i][j].grid(row = i, column = j)

window.mainloop()