class Aircraft(object):

    def __init__(self, max_ammo, base_damage, aircraft_type, ammo = 0):
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.aircraft_type = aircraft_type


    def fight(self):
        return self.ammo * self.base_damage
        self.ammo = 0


    def refill(self, number):
        if number > self.max_ammo:
            self.ammo += self.max_ammo
            number -= self.max_ammo
        else:
            self.ammo += number
            number = 0


    def get_type(self):
        return self.aircraft_type


    def get_status(self):
        #return "".join("Type: " + self.aircraft_type + ", Ammo:", self.ammo, ", Base Damage:", self.base_damage, ", All Damage:", self.fight())
        pass

sample = Aircraft(12, 5, "F16", 10)

print(sample.get_status())

    




class F16(Aircraft):
    pass





class F35(Aircraft):
    pass


    