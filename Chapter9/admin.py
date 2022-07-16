# Exercise 9-7. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# Admin: An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in
# 
# Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
# Add an attribute, privileges, that stores a list of strings like 
# "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s 
# set of privileges. Create an instance of Admin, and call your method.
from user import User

class Admin(User):
    def __init__(self, first_name, last_name, user_name, date_of_birth):
        super().__init__(first_name, last_name, user_name, date_of_birth)
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"\nUser has following privileges:")
        for i in self.privileges:
            print(f"\t{i}")


'''
meshvoid = Admin('Chingiz', 'Jumagulov', 'meshvoid', '1666.05.25')
meshvoid.describe_user()
meshvoid.show_privileges()
'''