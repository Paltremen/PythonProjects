current_users = ["Adam", "James", "Clive", "John", "Piper", "Ashley"]
new_users = ["Carly", "ADAM", "Bobby", "CLIVE", "Manny"]

for user in new_users:
    if user in current_users or user.upper() in current_users or user.lower() in current_users or user.title() in current_users:
        print(f"Sorry, {user}, that name is already registered.")
    else:
        print(f"Welcome to the site, {user}!")