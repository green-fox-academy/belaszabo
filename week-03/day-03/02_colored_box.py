from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
top = canvas.create_line(50, 50, 100, 50, fill = 'red')
right = canvas.create_line(100, 50, 100, 100, fill = 'green')
bottom = canvas.create_line(100, 100, 50, 100, fill = 'blue')
left = canvas.create_line(50, 100, 50, 50, fill = 'yellow')

root.mainloop()