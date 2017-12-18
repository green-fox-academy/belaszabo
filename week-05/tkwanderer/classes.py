from tkinter import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

class MainScreen(object):
    def __init__(self):
        self.map_tiles = [
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")

    def draw_table(self):
        for i in range(len(self.map_tiles)):
            for j in range(len(self.map_tiles[i])):
                x = i * 72
                y = j * 72
                if self.map_tiles[j][i] == 0:
                    canvas.create_image(x, y, anchor = NW, image = self.floor)
                else:
                    canvas.create_image(x, y, anchor = NW, image = self.wall)

class Character(object):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

class Hero(Character):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.hero_image = PhotoImage(file = "hero-down.png") 
        canvas.create_image(self.pos_x, self.pos_y, anchor = NW, image = self.hero_image)

screen = MainScreen()
screen.draw_table()
hero = Hero()

root.mainloop()
