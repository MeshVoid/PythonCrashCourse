# Exercise 5-1. From the book Python Crash Course 2nd Edition by Erick Matthews

# Conditional Tests: Write a series of conditional tests. Print a statement describing 
# each test and your prediction for the results of each test. 

# Your code should look something like this:

"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

"""
# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.

# Exercise 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
# Have at least one True and one False result for each of the following:

# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, 
#   greater than and less than, greater than or equal to, 
#   and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list


name = 'Mikey'
print(f"\nname = {name}")
print(f"Is name == 'Nina'. I predict {name == 'Nina'}.")
print(f"\nname = {name}")
print(f"Is name == 'Mikey'. I predict {name == 'Mikey'}.")

print(f"Is there a string value of 'Dick' in name? I predict {'Dick' in name}.")

print(f"\nIs name.lower() == 'mikey'? I predict {name.lower() == 'mikey'}.")

print(f"\nLets check if 'Stacey' is != name. I predict {'stacey' == name}.")

print(f"\nLets check if 'mikey'.title() is == name. I predict {'mikey'.title() == name}.")

your_age = 25

print(f"\nVariable your_age = {your_age}")
print(f"Is your_age >= 12? I predict: {your_age >= 12}.")
print(f"Is your_age == 25? I predict: {your_age == 25}.")
print(f"Is your_age == 23? I predict: {your_age == 23}.")
print(f"Is your_age < 90? I predict: {your_age < 90}.")
print(f"Is your_age < 90? I predict: {your_age < 90}.")
print(f"Is your_age >= 90? I predict: {your_age >= 90}.")





car_brands = ['bmw', 'audi', 'nissan', 'porsche', 'volvo']
print(f"\nWe have a list called car_brands = {car_brands}")
print(f"\nLet's check if 'toyota' is in the list shall we?")

if 'toyota' in car_brands:
    print('Yup, there is definately a toyota in the list')
else:
    print('Nope, no toyotas there, sadly')


print(f"\nIs there a 'BMW' in the list? I predict: {'BMW' in car_brands}.")
print(f"Oh no! But if we use upper() method on the car_brands[0] and check? I predict: {'BMW' in car_brands[0].upper()}.")
print(f"There we go!")
print(f"\nIs there an 'audi' and 'nissan' in the list? I predict: {'audi' and 'nissan' in car_brands}.")
print(f"Hell yeah there is!")
