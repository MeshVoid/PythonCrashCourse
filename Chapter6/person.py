# Exercise 6-1. From the book Python Crash Course 2nd Edition by Erick Matthews

# Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.

# Print each piece of information stored in your dictionary.

person = {
    'name': 'William', 
    'last name': 'Wallace',
    'age': '35', 
    'country': 'Scotland', 
    'city': 'Elderslie'
}


print(f"The name is:{person['name']}")
print(f"The last name is:{person['last name']}")
print(f"He died when he was:{person['age']}")
print(f"He was born in:{person['city']}")
