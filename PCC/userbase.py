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

class Administrator(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privilege_set = Privileges()


class Privileges:
    def __init__(self, privileges = ["can ban users", "can edit messages", "can register users"]):
        self.privileges = privileges

    def show_privileges(self):
        print("The admin has the following privileges: ")
        for privilege in self.privileges:
            print(privilege)