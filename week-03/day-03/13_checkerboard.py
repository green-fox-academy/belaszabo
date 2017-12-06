from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def draw_lines(x, y):
    for i in range(8):
        line1 = canvas.create_line(x, 0, x, 300)
        line2 = canvas.create_line(0, y, 300, y)
        x += 40
        y += 40

draw_lines(40,40)

root.mainloop()