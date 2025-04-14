from justuser import User

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