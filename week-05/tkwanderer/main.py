from tkinter import *
from classes import MainScreen

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

screen = MainScreen()
screen.draw_table()

root.mainloop()
