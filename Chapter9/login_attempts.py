# Exercise 9-5. From the book Python Crash Course 2nd Edition by Erick Matthews

# Login Attempts: Add an attribute called login_attempts to your Userclass
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1.
#
# Write another method called reset_login_attempts()
# that resets the value of login_attemptsto 0.Make an instance of the
# User class and call increment_login_attempts()several times. Print the
# value of login_attempts to make sure it was incremented properly, and
# then call reset_login_attempts(). Print login_attempts again to make sure
# it was reset to 0.



class User:
    '''User class to store all user data'''
    def __init__(self, first_name, last_name, 
                user_name, date_of_birth, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.login_attempts = int(login_attempts)
    
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

    def show_login_attempts(self):
        print(f"User tried to log in: {self.login_attempts} times in a row.")

    def increment_login_attempts(self, number=1):
        self.login_attempts += number
    
    def reset_login_attempts(self):
        self.login_attempts = 0


meshvoid = User('Chingiz', 'Jumagulov', 'meshvoid', '25.05.1666', 12)
meshvoid.describe_user()
meshvoid.show_login_attempts()
meshvoid.increment_login_attempts(12)
meshvoid.show_login_attempts()
meshvoid.reset_login_attempts()
meshvoid.show_login_attempts()
