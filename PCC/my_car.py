from car import Car as C
from electric_car import ElectricCar as EC
my_new_car = C("audi", "a4", 2024)
my_new_car.get_descriptive_name()
my_new_car.odometer_reading  = 23
my_new_car.read_odometer()


my_leaf = EC("nissan", "leaf", 2024) # no need to import Battery
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()

import car
newer_car = car.Car("lada", "niva", 1999)
newer_car.get_descriptive_name()

# from car import *
