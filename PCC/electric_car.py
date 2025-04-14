from car import Car

class Battery:
    def __init__(self, capacity=40):
        self.capacity = capacity
    def describe_battery(self):
        print(f"The car has a {self.capacity}-kWh battery.")
    def upgrade_battery(self):
        self.capacity = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_with_gas(self):
        print(f"This car doesn't have a gas tank!")
    def get_range(self):
        if self.battery.capacity == 40:
            range = 150
        elif self.battery.capacity == 65:
            range = 225
        print(f"This car can go about {range} miles on this battery.")