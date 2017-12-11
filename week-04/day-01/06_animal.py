class Animal(object):
    def __init__(self, hunger = 50, thirst = 50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

lion = Animal(60, 78)

print(lion.hunger)
print(lion.thirst)

lion.eat()

print(lion.hunger)