from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def draw_that(a):
    for i in range(16):
        x = 0
        y = 0
        purple = canvas.create_line(x+300-i*a, y, x+300, y+300-i*a, fill = 'purple')
    for i in range(16):
        x = 0
        y = 0
        green = canvas.create_line(x+300-i*a, y+300, x, y+300-i*a, fill = 'green')

draw_that(20)

root.mainloop()