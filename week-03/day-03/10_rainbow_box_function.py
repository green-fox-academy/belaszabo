from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def draw_square(x, color):
    square = canvas.create_rectangle(150-x/2, 150-x/2, 150+x/2, 150+x/2, fill = color)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
a = -300

for i in range(0, len(rainbow)):
    a +=20
    draw_square(a, rainbow[i])

root.mainloop()