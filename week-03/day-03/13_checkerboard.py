from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def draw_board(a):
    for i in range(8):
        y = 0
        y += i * a
        if i % 2 == 0:
            for i in range(4):
                x = 0
                x += i * a * 2
                black = canvas.create_rectangle(x, y, x + a, y + a, fill = 'black')
                white = canvas.create_rectangle(x + a, y, x + 2 * a, y + a, fill = 'white')
        else:
            for i in range(4):
                x = 0
                x += i * a * 2
                black = canvas.create_rectangle(x, y, x + a, y + a, fill = 'white')
                white = canvas.create_rectangle(x + a, y, x + 2 * a, y + a, fill = 'black')
        
draw_board(37)

root.mainloop()