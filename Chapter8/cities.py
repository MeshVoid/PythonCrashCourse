# Exercise 8-5. From the book Python Crash Course 2nd Edition by Erick Matthews

# Cities: Write a function called describe_city() that accepts the name of a 
# city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not 
# in the default country.


def describe_city(city = "Almaty", country = "Kazakhstan"):
    # Prints a message with a city name and it's country
    print(f"{city.title()} is situated in {country}")


describe_city("Paris","France")
describe_city()
describe_city("Washington", country="USA", )

