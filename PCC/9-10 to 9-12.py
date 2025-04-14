import restaurant

rest1 = restaurant.Restaurant("McDonalds", "fastfood")
rest1.describe_restaurant()
"""
from userbase import Administrator
phil = Administrator("phil", "voeal", 26, "antarctica") # no need to import parent object

phil.privilege_set.show_privileges()
"""

from justuser import User
from otherusers import Administrator

phil = Administrator("phil", "voeal", 26, "antarctica") # needed to add User to otherusers.py

phil.privilege_set.show_privileges()