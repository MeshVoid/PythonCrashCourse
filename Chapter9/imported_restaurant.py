# Exercise 9-10. From the book Python Crash Course 2nd Edition by Erick Matthews

# Imported Restaurant: Using your latest Restaurant class, 
# store it in a module. Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods 
# to show that the import statement is working properly.

from restaurant import Restaurant

bistro = Restaurant("Markie's bistro", 'neopolitanian')
bistro.describe_restaurant()