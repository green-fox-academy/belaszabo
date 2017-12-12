class Tree(object):


    def __init__(self, color, water = 0, needs_water = True):
        self.color = color
        self.water = water
        if water > 5:
            self.needs_water = False
        else:
            self.needs_water = True


    def status(self):
        if self.water > 5:
            self.needs_water = False
        else:
            self.needs_water = True

        if self.needs_water is True:
            print("The " + self.color + " Tree needs water")
        else:
            print("The " + self.color + " Tree doesn't need water")
            