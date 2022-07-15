# Exercise 9-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in 
# Exercise 9-7. Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.


class User:
    '''User class to store all user data'''
    def __init__(self, first_name, last_name, 
                user_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.date_of_birth = date_of_birth
    
    def describe_user(self):
        ''' Print user account information'''
        print(f"\nUser information: ")
        print(f"First name: {self.first_name.title()}.")
        print(f"Last name: {self.last_name.title()}.")
        print(f"Username: {self.user_name}.")
        print(f"Date of birth: {self.date_of_birth}.")
    
    def greet_user(self):
        '''Greet user with a message'''
        print(f"\nHello there, {self.user_name}!")
        print(f"Welcome to the system!")


class Privileges:
    """Priviliges class that a user or any other class can have"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print a message with user privileges"""
        print(f"\nUser has following privileges:")
        for i in self.privileges:
            print(f"\t{i}")


class Admin(User):
    """Admin class that inherits from the User class that has elevated privileges"""
    def __init__(self, first_name, last_name, user_name, date_of_birth):
        super().__init__(first_name, last_name, user_name, date_of_birth)
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.privileges = Privileges()


meshvoid = Admin('Chingiz', 'Jumagulov', 'meshvoid', '1666.06.06')
meshvoid.greet_user()
meshvoid.describe_user()
meshvoid.privileges.show_privileges()