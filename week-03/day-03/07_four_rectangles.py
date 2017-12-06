from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
rec1 = canvas.create_rectangle(10, 10, 50, 50, fill = 'green')
rec2 = canvas.create_rectangle(100, 80, 180, 200, fill = 'blue')
rec3 = canvas.create_rectangle(200, 200, 240, 280, fill = 'red')
rec4 = canvas.create_rectangle(130, 80, 150, 150, fill = 'yellow')

root.mainloop()