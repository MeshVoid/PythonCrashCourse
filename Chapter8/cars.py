# Exercise 8-14. From the book Python Crash Course 2nd Edition by Erick Matthews

# Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the func-tion with the required information and two other name-value pairs, 
# such as a color or an optional feature. Your function should work for a call like this one:
# 
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 
# Print the dictionary that’s returned to make sure all the information was stored correctly

def make_car(manufacturer, model, **kwargs):
    '''Build a dictionary with car data in it'''
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

print(make_car('subaru', 'forester'))

print(make_car('subaru', 'forester', released = '2008', mileage = 200000, tow_package = False, color = 'Green'))
