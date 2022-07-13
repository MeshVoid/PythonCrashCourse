# Exercise 8-6. From the book Python Crash Course 2nd Edition by Erick Matthews

# City Names: Write a function called city_country() that takes in the name of 
# a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, 
# and print the values that are returned.

def city_country(city_name='Santiago', country='Chile'):
    print(f"{city_name}, {country}")

city_country()
city_country('Almaty','Kazakhstan')
city_country('Saint-Petersburg','Russia')