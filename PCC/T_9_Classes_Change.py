class Car: 
    def __init__(self, make, model, year):
        self.make = make # These are VARIABLES, therefore do not need parentheses () after when accessing
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # This is a FUNCTION/METHOD, need parentheses
        print(f"This car is a {self.year} {self.make} {self.model}.")

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

car1 = Car("Audi", "A4", 2024)
car1.get_descriptive_name()
# car1.odomoter_reading = 23 # Update directly in instance
# car1.update_odometer(20) # Update via method
car1.increment_odometer(50)
car1.increment_odometer(-50)
car1.read_odometer()