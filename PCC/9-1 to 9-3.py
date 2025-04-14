''' 9.1 to 9.2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} cuisine restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Wendy's", "American")
restaurant2 = Restaurant("Hell's Kitchen", "British")
restaurant3 = Restaurant("Rosopomodoro", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
'''

class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.country}.")
    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}!")

user1 = User("Peter", "Parker", 23, "America")
user1.describe_user()
user1.greet_user()

user2 = User("Bruce", "Wayne", 30, "America")
user2.describe_user()
user2.greet_user()

user3 = User("Steve", "Rodgers", 35, "America")
user3.describe_user()
user3.greet_user()