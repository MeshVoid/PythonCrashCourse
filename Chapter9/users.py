# Exercise 9-3. From the book Python Crash Course 2nd Edition by Erick Matthews

# Users: Make a class called User. Create two attributes called:
# first_nameand last_name, and then create several other attributes 
# that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized 
# greeting to the user.Create several instances representing different 
# users, and call both methods for each user.


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



user_1 = User('Chingiz', 'Jumagulov', 'meshvoid', '25.05.1666')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Billie', 'Thornton', 'billthemegaman111', '23.01.1987')
user_2.describe_user()
user_2.greet_user()


user_3 = User('Timur', 'Smith', 'sexyboi666', '22.03.1967')
user_3.describe_user()
user_3.greet_user()