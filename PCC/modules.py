import modeller
car1 = modeller.car_profile("bmw", "beetle", year=1933, country="germany")
print(car1)
#If you do it this way, it imports the entire file and executes it

from modeller import car_profile
car2 = car_profile("lada", "niva", year=1999, country="russia")
print(car2)
# Imports a specific function only

import modeller as md
car3 = md.car_profile("chrysler", "pacifica", year=2025, country="USA")
print(car3)
# Alias for a module

from modeller import car_profile as cp
car4 = cp("fiat", "palio", year=1998, country="italy")
print(car4)
# Alias for a function

from modeller import *
car5 = car_profile("kia", "ceed", year=2020, country="south korea")
print(car5)
# Imports everything in a module natively