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