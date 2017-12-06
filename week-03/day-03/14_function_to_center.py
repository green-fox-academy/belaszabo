from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
def drawer():
    diagonal = canvas.create_line(300, 0, 0, 300)
    for i in range(15):
        a = 20
        line1 = canvas.create_line(0+i*a, 0, 300-i*a, 300)
        line2 = canvas.create_line(0, 0+i*a, 300, 300-i*a)

drawer()

root.mainloop()