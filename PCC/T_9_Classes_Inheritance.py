class Car: 
    def __init__(self, make, model, year):
        self.make = make # These are VARIABLES, therefore do not need parentheses () after when accessing
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # This is a FUNCTION/METHOD, need parentheses
        print(f"This car is a {self.year} {self.make.title()} {self.model.title()}.")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage <= self.odometer_reading:
            print(f"You can't roll back an odometer! Type another value.")
        else:
            self.odometer_reading = mileage
            print(f"Value updated to {self.odometer_reading}.")

    def increment_odometer(self, increment):
        if increment <=0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += increment
    
    def fill_with_gas(self):
        print(f"Filled with gas!")

class Battery:
    def __init__(self, capacity=40):
        self.capacity = capacity
    def describe_battery(self):
        print(f"The car has a {self.capacity}-kWh battery.")


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

tesla = ElectricCar("tesla", "cybertruck", 2023)
audi = Car("audi", "a8", 2024)
tesla.get_descriptive_name()

audi.fill_with_gas()
tesla.fill_with_gas()

tesla.battery.describe_battery()
tesla.get_range()