# Exercise 9-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in 
# Exercise 9-7. Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

from user import User
from admin import Admin


class Privileges():
    """Priviliges class that a user or any other class can have"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print a message with user privileges"""
        print(f"\nUser has following privileges:")
        for i in self.privileges:
            print(f"\t{i}")


meshvoid = Admin('Chingiz', 'Jumagulov', 'meshvoid', '1666.06.06')
meshvoid.greet_user()
meshvoid.describe_user()
meshvoid.privileges.show_privileges()