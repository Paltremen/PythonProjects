""" 9.13
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))
d6 = Die()
d10 = Die(sides=10)
d20 = Die(sides=20)

for i in range (10):
    d20.roll_die()
"""

combinations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "x", "q", "t"]

from random import choice
winner = "52xt"
tries = 0
while True:
    my_ticket = ""
    for i in range(4):
        my_ticket += str(choice(combinations))
    if my_ticket != winner:
        tries += 1
        continue
    elif my_ticket == winner:
        print(f"You won! This took {tries} tries.")
        break