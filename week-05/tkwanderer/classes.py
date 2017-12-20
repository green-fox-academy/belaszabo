from tkinter import *
from random import randint

root = Tk()
canvas = Canvas(root, width = 820, height = 720)
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
        self.level = 1
        self.max_hp = 0
        self.current_hp = 0
        self.dp = 0
        self.sp = 0

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.hero_image = PhotoImage(file = "hero-down.png") 
        canvas.create_image(self.pos_x, self.pos_y, anchor = NW, image = self.hero_image)
        self.max_hp = 20 + 3 * randint(1, 6)
        self.current_hp = self.max_hp
        self.dp = 2 * randint(1, 6)
        self.sp = 5 + randint(1, 6)

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

    def level_up(self):
        self.hp += randint(1, 6)
        self.dp += randint(1, 6)
        self.sp += randint(1, 6)

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.skeleton_image = PhotoImage(file = "skeleton.png")
        self.max_hp = 2 * self.level * randint(1, 6)
        self.current_hp = self.max_hp
        self.dp = self.level / 2 * randint(1, 6)
        self.sp = self.level * randint(1, 6)

    def draw_skeleton(self):
        self.random_x = randint(1, 9)
        self.random_y = randint(0, 9)
        self.pos_x = self.random_x
        self.pos_y = self.random_y
        if screen.map_tiles[self.pos_y][self.pos_x] != 1:
            canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.skeleton_image)
        else:
            self.draw_skeleton()

class EnemyBoss(Enemy):
    def __init__(self):
        super().__init__()
        self.boss_image = PhotoImage(file = "boss.png")
        self.max_hp = 2 * self.level * randint(1, 6) + randint(1, 6)
        self.current_hp = self.max_hp
        self.dp = self.level / 2 * randint(1, 6) + (randint(1, 6) / 2)
        self.sp = self.level * randint(1, 6) + self.level
    
    def draw_boss(self):
        self.random_x = randint(7, 9)
        self.random_y = randint(7, 9)
        self.pos_x = self.random_x
        self.pos_y = self.random_y
        if screen.map_tiles[self.pos_y][self.pos_x] != 1:
            canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.boss_image)
        else:
            self.draw_boss()

class StatBox(object):
    def __init__(self):
        canvas.create_text(750, 20, text = "Hero lvl:")
        canvas.create_text(790, 20, text = hero.level)
        canvas.create_text(750, 40, text = "Hero HP:")
        canvas.create_text(790, 40, text = str(hero.current_hp) + " / " + str(hero.max_hp))
        canvas.create_text(750, 60, text = "Hero DP:")
        canvas.create_text(790, 60, text = hero.dp)
        canvas.create_text(750, 80, text = "Hero SP:")
        canvas.create_text(790, 80, text = hero.sp)

    def fighting(self):
        canvas.create_text(750, 120, text = "FIGHTING!!!")
        canvas.create_text(750, 140, text = "Enemy's HP:")

class Fight(object):
    def __init__(self):
        pass

    def is_hero_on_enemy_tile(self):
        if hero.pos_x == boss.pos_x and hero.pos_y == boss.pos_y:
            stat_box.fighting()

hero = Hero()
canvas.bind("<KeyPress>", hero.move)

canvas.focus_set()

screen = MainScreen()
screen.draw_table()
    
skeleton = Enemy()

for i in range(3):
    skeleton.draw_skeleton()

boss = EnemyBoss()
boss.draw_boss()

stat_box = StatBox()

fight = Fight()
fight.is_hero_on_enemy_tile()

root.mainloop()
