from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
def draw_sky():
    for _ in range(100):
        a = random.randint(0, 255)
        color = '#%02x%02x%02x' % (a, a, a)
        x = random.randint(0, 290)
        y = random.randint(0, 290)
        canvas.create_rectangle(x, y, x+5, y+5, fill=color)

draw_sky()

root.mainloop()