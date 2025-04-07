""" 8-12 (1)
def sandwich_toppings():
    print(f"Please enter any topics you'd like")
    toppings = tuple(input("Your toppings: ").split(", "))
    if toppings == "":
        print("Please enter toppings.")
        
    print(f"Your sandwich contains the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")

sandwich_toppings()
"""
""" 8-12 (2)
def sandwich_toppings(*toppings):
    print(f"Your sandwich contains the following toppings:")
    for topping in toppings:
        print(f"\t{topping.title()}")

sandwich_toppings("salami", "cheese", "lettuce")
"""
""" 8-13
def build_profile(first, last, **user_info):
    profile = {
        "first name": first.title(),
        "last name": last.title()
    }
    profile.update(user_info)
    return profile
user_profile = build_profile("john", "doe", location="london", field="linguistics", age=30)
# So first it creates a dictionary called the parameter name and adds the kwargs to it
# And then adds the other values
print(user_profile)
"""
""" 8-14
def car_profile(manufacturer, model, **details):
    profile = {
        "manufacturer": manufacturer,
        "model": model
    }
    profile.update(details)
    return profile
car1 = car_profile("Audi", "A1", year=2018, car_class="supermini", price=50_000, tow_package=True)
print(car1)
"""