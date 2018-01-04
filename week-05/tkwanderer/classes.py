from tkinter import *
from random import randint
from time import sleep

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
        self.size = 72
        self.level = 1
        self.max_hp = 0
        self.current_hp = 0
        self.dp = 0
        self.sp = 0

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.pos_x = 0
        self.pos_y = 0
        self.hero_image = PhotoImage(file = "hero-down.png") 
        canvas.create_image(self.pos_x, self.pos_y, anchor = NW, image = self.hero_image)
        self.max_hp = 20 + 3 * randint(1, 6)
        self.current_hp = self.max_hp
        self.dp = 2 * randint(1, 6)
        self.sp = 5 + randint(1, 6)

    def move(self, e):
        try:
            if e.keysym == "Right":
                self.hero_image = PhotoImage(file = "hero-right.png") 
                if self.pos_x <= 9 and screen.map_tiles[self.pos_y][self.pos_x + 1] == 0:
                    self.pos_x += 1
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
                else:
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            elif e.keysym == "Left":
                self.hero_image = PhotoImage(file = "hero-left.png")
                if self.pos_x >= 1 and screen.map_tiles[self.pos_y][self.pos_x - 1] == 0:
                    self.pos_x -= 1
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
                else:
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            elif e.keysym == "Down":
                self.hero_image = PhotoImage(file = "hero-down.png") 
                if self.pos_y <= 9 and screen.map_tiles[self.pos_y + 1][self.pos_x] == 0:
                    self.pos_y += 1
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
                else:
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            elif e.keysym == "Up":
                self.hero_image = PhotoImage(file = "hero-up.png") 
                if self.pos_y >= 1 and screen.map_tiles[self.pos_y - 1][self.pos_x] == 0:
                    self.pos_y -= 1
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
                else:
                    canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.hero_image)
            fight.is_hero_on_boss_tile()
            fight.is_hero_on_skeleton_tile()
        except IndexError:
            pass

    def level_up(self):
        self.hp += randint(1, 6)
        self.dp += randint(1, 6)
        self.sp += randint(1, 6)

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.image = PhotoImage(file = "skeleton.png")
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
            canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)
        else:
            self.draw_skeleton()

    def move(self):
        self.direction = randint(1, 4)
        if self.direction == 1:
            if self.pos_x <= 8 and screen.map_tiles[self.pos_y][self.pos_x + 1] == 0:
                self.pos_x += 1
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)
        elif self.direction == 2:
            if self.pos_x >= 1 and screen.map_tiles[self.pos_y][self.pos_x - 1] == 0:
                self.pos_x -= 1
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)
        elif self.direction == 3:
            if self.pos_y <= 8 and screen.map_tiles[self.pos_y + 1][self.pos_x] == 0:
                self.pos_y += 1
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)
        elif self.direction == 4:
            if self.pos_y >= 1 and screen.map_tiles[self.pos_y - 1][self.pos_x] == 0:
                self.pos_y -= 1
                canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)

class EnemyBoss(Enemy):
    def __init__(self):
        super().__init__()
        self.image = PhotoImage(file = "boss.png")
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
            canvas.create_image(self.pos_x * self.size, self.pos_y * self.size, anchor = NW, image = self.image)
        else:
            self.draw_boss()

class StatBox(object):
    def __init__(self):
        canvas.create_text(770, 20, text = "Hero lvl: " + str(hero.level))
        canvas.create_text(770, 40, text = "Hero HP: " + str(hero.current_hp) + " / " + str(hero.max_hp))
        canvas.create_text(770, 60, text = "Hero DP: " + str(hero.dp))
        canvas.create_text(770, 80, text = "Hero SP: " + str(hero.sp))

    def fighting(self):
        canvas.create_text(770, 120, text = "FIGHTING!!!")
        canvas.create_text(770, 140, text = "Enemy's HP: ")

class Fight(object):
    def is_hero_on_boss_tile(self):
        while hero.pos_x == boss.pos_x and hero.pos_y == boss.pos_y and hero.current_hp > 0 and boss.current_hp > 0:
            stat_box.fighting()
            self.enemy_fight()

    def is_hero_on_skeleton_tile(self):
        while hero.pos_x == skeleton.pos_x and hero.pos_y == skeleton.pos_y and hero.current_hp > 0 and skeleton.current_hp > 0:
            stat_box.fighting()
            self.enemy_fight()

    def enemy_fight(self, e):
        self.sv = hero.sp + randint(1, 6) * 2
        self.boss_sv = boss.sp + randint(1, 6) * 2
        if e.keysym == "space":
            if self.sv > boss.dp:
                boss.current_hp -= self.sv
            if self.boss_sv > hero.dp:
                hero.current_hp -= self.boss_sv

hero = Hero()

screen = MainScreen()
screen.draw_table()
    
skeleton = Enemy()

for i in range(3):
    skeleton.draw_skeleton()

# skeleton.move()

boss = EnemyBoss()
boss.draw_boss()

boss.move()

stat_box = StatBox()

fight = Fight()

canvas.bind("<KeyPress>", hero.move, fight.enemy_fight)

canvas.focus_set()


root.mainloop()
