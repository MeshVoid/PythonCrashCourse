"""Class that store all default user data"""
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