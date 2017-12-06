from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def draw_squares():
    b = 2
    for _ in range(6):
        a = 0
        b *= 2
        a += b
        square = canvas.create_rectangle(a, a, a+b, a+b, fill = 'purple')

draw_squares()

root.mainloop()