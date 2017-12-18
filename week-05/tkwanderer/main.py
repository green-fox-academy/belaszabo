from tkinter import *
from classes import MainScreen, Character, Hero

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

hero = Hero()
canvas.bind("<KeyPress>", hero.move)

canvas.focus_set()

screen = MainScreen()
screen.draw_table()

root.mainloop()
