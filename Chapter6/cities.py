# Exercise 6-11. From the book Python Crash Course 2nd Edition by Erick Matthews.

# Cities: Make a dictionary called cities. Use the names of three cities as keys
# in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one
# fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city and all of the
# information you have stored about it.

cities = {
    'New York': {
        'country': 'USA',
        'founded in': 1624,
        'population': '8.38 million',
        'fact': '''More than 800 languages are spoken in New York City, 
    making it the most linguistically diverse city in the world.'''
    },
    'Moscow': {
        'country': 'Russia',
        'founded in': 1147,
        'population': '8.38 million',
        'fact': '''Trains with the most frequency in the world are 
    found in Moscow.'''
    },
    'Almaty': {
        'country': 'Russia',
        'founded in': 1147,
        'population': '8.38 million',
        'fact': '''TV tower is a visit card of Almaty, one of the 
    tallest TV towers in the world.'''
    }
}

for city_name, city_info in cities.items():
    print(f"\n{city_name}:")
    print(f"\tSituated in: {city_info['country']}")
    print(f"\tFounded in: {city_info['founded in']}")
    print(f"\tHas a population of: {city_info['population']}")
    print(f"\t{city_info['fact']}")
