# Exercise 9-11. From the book Python Crash Course 2nd Edition by Erick Matthews

# Imported Admin: Start with your work from Exercise 9-8 (page 173). 
# Store the classes User, Privileges, and Admin in one module. 
# Create a sepa-rate file, make an Admin instance, and call 
# show_privileges() to show that everything is working correctly.

# Exercise 9-12. From the book Python Crash Course 2nd Edition by Erick Matthews

# Multiple Modules: Store the User class in one module, and store the 
# Privileges and Admin classes in a separate module. In a separate file, 
# create an Admin instance and call show_privileges() to show that 
# everything is still working correctly.

from admin import Admin

meshvoid = Admin('Chingiz', 'Jumagulov', 'GOD', '666.06.06')
meshvoid.describe_user()
meshvoid.show_privileges()