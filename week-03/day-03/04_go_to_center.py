from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def draw_line(x, y):
    line = canvas.create_line(x, y, 150, 150)

draw_line(0, 0)
draw_line(45, 5)
draw_line(78, 100)

root.mainloop()