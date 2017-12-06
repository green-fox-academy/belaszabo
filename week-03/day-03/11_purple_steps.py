from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def draw_square(a, b):
    square = canvas.create_rectangle(a, a, b, b, fill = 'purple')

a = 10
b = 20

for i in range(19):
    a += 10
    b += 10
    draw_square(a, b)

root.mainloop()