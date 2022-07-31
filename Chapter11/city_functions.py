# Exercise 11-1 and 11-2 From the book Python Crash Course 2nd Edition by Erick Matthews

#  City, Country: Write a function that accepts two parameters: 
# a city name and a country name. 
# The function should return a single string of the form City, Country, 
# such as Santiago, Chile. Store the function in a module called 
# city_functions.py.

# Population: Modify your function so it requires a third parameter, 
# population. It should now return a single string of the form City, 
# Country –  population xxx, such as Santiago, Chile – population 5000000. 
# Run test_cities.py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. 
# Run test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that veri-fies you 
# can call your function with the values 'santiago', 'chile', and 
# 'population=5000000'. Run test_cities.py again, and make sure this new test 
# passes



def city_functions(city_name, country_name, population=''):
    if population:
        string = f"{city_name}, {country_name}"
        return string.title() + f" - population: {population}"
    else:
        string = f"{city_name}, {country_name}"
        return string.title()