''' 9.4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} cuisine restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def change_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant1 = Restaurant("Wendy's", "American")
print(restaurant1.number_served)
restaurant1.number_served = 35
print(restaurant1.number_served)
restaurant1.change_number_served(40)
print(restaurant1.number_served)
restaurant1.increment_number_served(5)
print(restaurant1.number_served)
'''
class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.country}.")

    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Peter", "Parker", 23, "America")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)