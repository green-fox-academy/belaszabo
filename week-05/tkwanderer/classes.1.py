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
        self.size = 72

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.hero_image = PhotoImage(file = "hero-down.png") 
        canvas.create_image(self.pos_x, self.pos_y, anchor = NW, image = self.hero_image)

    def move(self, e):
        if e.keysym == "Right":
            if self.pos_x <= 9 and screen.map_tiles[self.pos_y][self.pos_x + 1] == 0:
                self.pos_x += 1
                self.hero_image = PhotoImage(file = "hero-right.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            else:
                self.hero_image = PhotoImage(file = "hero-right.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
        elif e.keysym == "Left":
            if self.pos_x >= 1 and screen.map_tiles[self.pos_y][self.pos_x - 1] == 0:
                self.hero_image = PhotoImage(file = "hero-left.png")
                self.pos_x -= 1
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            else:
                self.hero_image = PhotoImage(file = "hero-left.png")
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
        elif e.keysym == "Down":
            if self.pos_y <= 9 and screen.map_tiles[self.pos_y + 1][self.pos_x] == 0:
                self.pos_y += 1
                self.hero_image = PhotoImage(file = "hero-down.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            else:
                self.hero_image = PhotoImage(file = "hero-down.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
        elif e.keysym == "Up":
            if self.pos_y >= 1 and screen.map_tiles[self.pos_y - 1][self.pos_x] == 0:
                self.pos_y -= 1
                self.hero_image = PhotoImage(file = "hero-up.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            else:
                self.hero_image = PhotoImage(file = "hero-up.png") 
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)

class Enemy(Character):
    pass

class EnemyBoss(Enemy):
    pass

hero = Hero()
canvas.bind("<KeyPress>", hero.move)

canvas.focus_set()

screen = MainScreen()
screen.draw_table()

root.mainloop()
