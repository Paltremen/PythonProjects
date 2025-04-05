# Three ways to exit a while loop:
'''
current_toppings = []
while True:
    added_topping = input("What topping do you want? ")
    if added_topping == "quit":
        print(f"You've added {current_toppings}")
        break
    current_toppings.append(added_topping)
    print(f"Current toppings: {current_toppings}")
'''

'''
current_toppings = []
added_topping = ""
while added_topping != "quit":
    added_topping = input("What topping do you want? ")
    if added_topping != "quit":
        current_toppings.append(added_topping)
    print(f"Current toppings: {current_toppings}")
'''

'''
current_toppings = []
active = True
while active:
    added_topping = input("What topping do you want? ")
    if added_topping != "quit":
        current_toppings.append(added_topping)
    else:
        active = False
    print(f"Current toppings: {current_toppings}")'
'''

while True:
    age = input("What is your age? ")
    if age == "quit":
        break
    elif int(age) <= 3:
        print("No entrance fee!")
    elif int(age) <= 12:
        print("The entrance fee is $10")
    elif int(age) > 12:
        print("The entrance fee is $15")