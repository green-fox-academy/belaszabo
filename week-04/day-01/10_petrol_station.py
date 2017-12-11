class Station(object):
    def __init__(self, gas_amount = 20000):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity

class Car(object):
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity

station = Station()
car = Car()

print("Station's gas amount:", station.gas_amount)
print("Car's gas amount:", car.gas_amount, "Car's capacity:", car.capacity)

station.refill(car)

print("Station's gas amount:", station.gas_amount)
print("Car's gas amount:", car.gas_amount, "Car's capacity:", car.capacity)
