class Character(object):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0


class Hero(Character):
    def __init__(self):
        self.pos_x = 0
        self.pos_x = 0
        self.hero_image = PhotoImage(file = "hero-down.png") 
        canvas.create_image(self.pos_x, self.pos_y, anchor = NW, image = self.hero_image)
