class Sharpie(object):
    def __init__(self, color, width, ink_amount = 100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount -= 1

sharpie = Sharpie("blue", 20)
print(sharpie.ink_amount)
print(sharpie.color)
sharpie.use()
print(sharpie.ink_amount)
